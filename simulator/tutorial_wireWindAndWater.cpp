#include <agxOSG/ExampleApplication.h>
#include <agxOSG/SCCameraManipulator.h>

#include <agxModel/WindAndWaterController.h>

#include <agxWire/Wire.h>
#include <agxWire/WireController.h>
#include <agxWire/Node.h>

#include <agxOSG/WireRenderer.h>

#include <agxRender/Color.h>

#include "tutorialUtils.h"
#include <agxSDK/GeometryFilter.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

agx::RigidBodyRef cylL[5]; // 左側の剛体を格納
agx::RigidBodyRef cylR[5]; // 右側の剛体を格納
agx::Vec3 wireNodePosition[];	// ワイヤーのNode(分割点)を格納
vector<float> nodePosition;	// 経路情報のファイルから取得したNodeの座標値を格納
vector<agx::Vec3> outputNodePos; // 出力時のWireのNodeを格納
agxWire::Wire* wire; // 経路情報に従い表示するワイヤー
bool rerunTest = false;

namespace
{

	/**
	Create visual representation of the water.
	*/
	agxOSG::GeometryNode* creatVisual(agxCollide::Geometry* cylinderGeometry, osg::Group* root)
	{
		agxOSG::GeometryNode* node = tutorialUtils::createVisual(cylinderGeometry, root);
		const agx::Vec4f color = agxRender::Color::GreenYellow();
		agxOSG::setDiffuseColor(node, color);


		return node;
	}
}

// 区切り文字を取り除く
vector<string> split(string& input, char delimiter = ',')
{
	istringstream stream(input);
	string field;
	vector<string> result;
	size_t c;

	// 文字列をコンマ<,>区切り
	while (getline(stream, field, delimiter)) {
		// 括弧< [ >とスペース< >を削除
		while ((c = field.find_first_of("[ ")) != string::npos) {
			field.erase(c, 1);
		}
		// 括弧< ] >とスペース< >を削除
		while ((c = field.find_first_of(" ]")) != string::npos) {
			field.erase(c, 1);
		}
		while ((c = field.find_first_of(")")) != string::npos) {
			field.erase(c, 1);
		}
		while ((c = field.find_first_of("(")) != string::npos) {
			field.erase(c, 1);
		}

		result.push_back(field);
	}

	return result;
}

// 座標値以外の情報ならtrue
// 酷い実装なのであとで書き換える
bool checkLR(std::string check) {
	bool ans = false;
	if (check == "LT" || check == "LF" || check == "LM" || check == "LR" || check == "LL" ||
		check == "RT" || check == "RF" || check == "RM" || check == "RR" || check == "RL") {
		ans = true;
	}
	return ans;

}

// txtファイルから経路情報の読み込み
// 引数に実行する経路情報のテキストファイル
vector<float> readFile(const string fileName) {
	std::ifstream ifs(fileName);
	std::string file;

	vector<float> position;

	// ifsの文字列を1行毎にfileへ
	while (getline(ifs, file)) {
		//　カンマなどの不要な文字を取り除く
		vector<string> strvec = split(file);
		// vectorの要素が座標値以外なら次のループ
		if (checkLR(strvec.at(0))) {
			continue;
		}

		// 座標値をVectorに代入
		int sz = strvec.size();
		if (sz > 3) {
			sz = 3;
		}
		//for (int i = 0; i < strvec.size(); i++) {
		for (int i = 0; i < sz; i++) {
			// StringからFloatに変換
			position.push_back(std::stof(strvec.at(i)));
		}

	}
	std::cout << position.at(2) << endl;
	return position;
}

// Wireの全てのNodeを取得
// 後で中身のコメント残す
vector<agx::Vec3> getAllWireNode(agxWire::Wire* m_wire) {

	vector<agx::Vec3> nodeRoute;

	agxWire::RenderIterator renderIt = m_wire->getRenderBeginIterator();
	agxWire::RenderIterator renderEndIt = m_wire->getRenderEndIterator();

	while (renderIt != renderEndIt) {
		const agxWire::Node* node = *renderIt;
		agx::Vec3 nodePosition = node->getWorldPosition();
		nodeRoute.push_back(nodePosition);

		++renderIt;
	}
	return nodeRoute;
}

// 経路情報を出力
void outputNodeRoute(const string filePath) {

	std::ofstream ofs(filePath);

	agx::Vec3 pos = cylR[4]->getPosition();
	std::cout << pos.x() << endl;
	std::cout << pos.y() << endl;
	std::cout << pos.z() << endl;
	double posX = pos.x();
	double posY = pos.y();
	double px = posX + (0.9);
	double py = posY - 0.9;
	std::cout << px << endl;
	std::cout << py << endl;
	std::cout << posX << endl;
	ofs << std::to_string(px) << endl;
	ofs << std::to_string(py) << endl;
	ofs << std::to_string(posX) << endl;
	outputNodePos = getAllWireNode(wire);
	for (int i = 0; i < outputNodePos.size(); i++) {
	std:cout << outputNodePos[i] << endl;
		if (i == outputNodePos.size() - 1) {
			ofs << "( " + std::to_string(outputNodePos[i].x()) + ", "
				+ std::to_string(outputNodePos[i].y()) + ", "
				+ std::to_string(outputNodePos[i].z()) + " )";
		}
		else {
			ofs << "( " + std::to_string(outputNodePos[i].x()) + ", "
				+ std::to_string(outputNodePos[i].y()) + ", "
				+ std::to_string(outputNodePos[i].z()) + " )" << endl;
		}
	}


}


// EventListenerの設定
class KeyboardControl : public agxSDK::GuiEventListener {
public:
	// 引数に操作する剛体の配列
	KeyboardControl(agx::RigidBodyRef* LRigidBody, agx::RigidBodyRef* RRigidBody)
		:lBody(LRigidBody), rBody(RRigidBody)
	{
		// We only want to listen to keyboard events.
		setMask(agxSDK::GuiEventListener::KEYBOARD);
	}


	virtual bool keyboard(int key, unsigned int modKeyMask, float /*x*/, float /*y*/, bool keydown)
	{

		bool handled = false;
		double x_velocity = 0;				// x軸の速度
		double y_little_thumb_finger = 0;	// 小指と親指のy軸の速度
		double y_index_ring_finger = 0;		// 薬指と人差し指のy軸の速度
		double initialized = 10;


		if (!lBody->isValid()) {
			return false;
		}

		// 左右の剛体をx軸に狭める
		if (key == agxSDK::GuiEventListener::KEY_Left) {
			x_velocity = -initialized;
			y_little_thumb_finger = 0;
			y_index_ring_finger = 0;

			handled = true;

		}
		// 左右の剛体をx軸に広げる
		else if (key == agxSDK::GuiEventListener::KEY_Right) {
			x_velocity = initialized;
			y_little_thumb_finger = 0;
			y_index_ring_finger = 0;

			std::cout << "広げる" << endl;

			handled = true;
		}
		// 剛体をy軸に広げる
		else if (key == agxSDK::GuiEventListener::KEY_Up) {
			x_velocity = initialized;
			y_little_thumb_finger = initialized;
			y_index_ring_finger = initialized / 2.0;

			handled = true;
		}
		// 剛体をy軸に狭める
		else if (key == agxSDK::GuiEventListener::KEY_Down) {
			x_velocity = 0;
			y_little_thumb_finger = -initialized;
			y_index_ring_finger = -initialized / 2.0;

			handled = true;
		}
		// 剛体の動作を停止
		else if (key == agxSDK::GuiEventListener::KEY_Space) {
			x_velocity = 0;
			y_little_thumb_finger = 0;
			y_index_ring_finger = 0;

			handled = true;
		}
		else if (key == agxSDK::GuiEventListener::KEY_Shift_R) {
			agx::Vec3 cylPosition3 = cylR[4]->getPosition();

			double cylPosX = cylPosition3.x();
			double cylPosY = cylPosition3.y();

			double cylMovePosX = cylPosX + 0.9;
			double cylMovePosY = cylPosY - 0.9;

			std::cout << "出力するファイルパスを入力" << endl;
			string filePath;
			cin >> filePath;
			// 入力量を減らすためsyuuseiまでのパスを指定
			filePath = "c:\\Users\\hayashi\\Desktop\\stringRoute\\output\\" + filePath;
			outputNodeRoute(filePath);
		}
		else if (key == agxSDK::GuiEventListener::KEY_Shift_L) {
			rerunTest = true;
			string filePath;
			cin >> filePath;
		}

		// 剛体に速度を設定
		lBody[0]->setVelocity(agx::Vec3(-x_velocity, -y_little_thumb_finger, 0));
		lBody[1]->setVelocity(agx::Vec3(-x_velocity, -y_index_ring_finger, 0));
		lBody[2]->setVelocity(agx::Vec3(-x_velocity, 0, 0));
		lBody[3]->setVelocity(agx::Vec3(-x_velocity, y_index_ring_finger, 0));
		lBody[4]->setVelocity(agx::Vec3(-x_velocity, y_little_thumb_finger, 0));

		rBody[0]->setVelocity(agx::Vec3(x_velocity, -y_little_thumb_finger, 0));
		rBody[1]->setVelocity(agx::Vec3(x_velocity, -y_index_ring_finger, 0));
		rBody[2]->setVelocity(agx::Vec3(x_velocity, 0, 0));
		rBody[3]->setVelocity(agx::Vec3(x_velocity, y_index_ring_finger, 0));
		rBody[4]->setVelocity(agx::Vec3(x_velocity, y_little_thumb_finger, 0));
		return handled;
	}
private:
	agx::RigidBodyRef* lBody;
	agx::RigidBodyRef* rBody;
};

osg::Group* buildCylinder(agxSDK::Simulation* simulation, agxOSG::ExampleApplication* application)
{
	osg::Group* root = new osg::Group();

	// 再現を行う時間を設定
	simulation->agxSDK::Simulation::setTimeStep(1.0 / 7000.0);

	// 再現空間内の重力を設定
	agx::Vec3 gravity = agx::Vec3(0, 0, 0);
	simulation->setUniformGravity(gravity);


	// カメラの位置を指定
	agx::Vec3 eye = agx::Vec3(0, 0, 5.5);
	agx::Vec3 center = agx::Vec3(0, 0, 0);
	agx::Vec3 up = agx::Vec3(0, -1, 0);
	application->setCameraHome(eye, center, up);

	// Create a static box that will hold the end of each wire.
	double cylinderPos = -0.9; // 小指の剛体の初期座標
	double space = 0.45;	   // 剛体同士の生成間隔

	double x = 0.3;
	// 小指～親指の順に円柱を生成
	for (int i = 0; i < sizeof(cylR) / sizeof(cylR[0]); i++) {
		// 左側の円柱を生成
		cylL[i] = new agx::RigidBody(new agxCollide::Geometry(new agxCollide::Cylinder(0.08, 2.5)));
		//cylL[i]->setPosition(0.9 + x, cylinderPos, 0); //xの値を+-0.9からヒモを引き伸ばした値を加算する
		cylL[i]->setPosition(nodePosition.at(2) + x -0.05, cylinderPos, 0); //xの値を+-0.9からヒモを引き伸ばした値を加算する
		cylL[i]->setMotionControl(agx::RigidBody::KINEMATICS);
		cylL[i]->setRotation(agx::Quat::rotate(agx::Vec3::Y_AXIS(), agx::Vec3::Z_AXIS()));
		agxOSG::setDiffuseColor(agxOSG::createVisual(cylL[i], root), agxRender::Color::PaleGoldenrod());
		simulation->add(cylL[i]);

		// 右側の円柱を生成
		cylR[i] = new agx::RigidBody(new agxCollide::Geometry(new agxCollide::Cylinder(0.08, 2.5)));
		//cylR[i]->setPosition(-0.9 - x, cylinderPos, 0);	//xの値を+-0.9からヒモを引き伸ばした値を加算する
		cylR[i]->setPosition(-nodePosition.at(2) - x + 0.05, cylinderPos, 0);	//xの値を+-0.9からヒモを引き伸ばした値を加算する
		cylR[i]->setMotionControl(agx::RigidBody::KINEMATICS);
		cylR[i]->setRotation(agx::Quat::rotate(agx::Vec3::Y_AXIS(), agx::Vec3::Z_AXIS()));
		agxOSG::setDiffuseColor(agxOSG::createVisual(cylR[i], root), agxRender::Color::LightGoldenrodYellow());
		simulation->add(cylR[i]);

		// 次に生成する位置をずらす
		cylinderPos += space;
	}

	// 剛体にEventListenerを設定
	KeyboardControl* keyboard = new KeyboardControl(cylR, cylL);
	simulation->addEventListener(keyboard);


	// ワイヤーの端を接続するための剛体
	agx::RigidBodyRef connectWireRigidBody;
	connectWireRigidBody = new agx::RigidBody(new agxCollide::Geometry(new agxCollide::Box(0.01, 0.01, 0.01)));
	connectWireRigidBody->setPosition(nodePosition.at(3), nodePosition.at(4), nodePosition.at(5));
	simulation->add(connectWireRigidBody);
	agxOSG::createVisual(connectWireRigidBody, root);

	// wireモデルの生成
	double wireRadius = 0.01;	// ワイヤーの半径
	int wireResolutin = 1;		// ワイヤーの分割間隔

	wire = new agxWire::Wire(wireRadius, wireResolutin, true);
	
	// 剛体に接続。ヒモの最初と最後のノードからベクトルを求めて、接続位置を決定
	int sz = nodePosition.size();
	agx::Vec3 rt = agx::Vec3(nodePosition.at(6)-nodePosition.at(sz-3), nodePosition.at(7)-nodePosition.at(sz-2), nodePosition.at(8)-nodePosition.at(sz-1));
	rt = rt / rt.length() * 0.01;
	wire->add(new agxWire::BodyFixedNode(connectWireRigidBody, rt));	// 剛体に接続

	// 経路情報に応じたフリーノードの作成
	for (int i = 6; i < nodePosition.size(); i += 3) {
		wire->add(new agxWire::FreeNode(nodePosition.at(i), nodePosition.at(i + 1), nodePosition.at(i + 2)));
	}

	wire->add(new agxWire::BodyFixedNode(connectWireRigidBody, rt*(-1)));	// ワイヤーの反対側を剛体に接続
	simulation->add(wire);

	// ワイヤー同士の衝突判定
	agxWire::WireController::instance()->setEnableCollisions(wire, wire, true);


	agxOSG::WireRendererRef wireRenderer = new agxOSG::WireRenderer(wire, root);
	wireRenderer->setColor(agxRender::Color::GreenYellow());
	simulation->add(wireRenderer);

	return root;
}



// メインの実行部
int main(int argc, char** argv)
{
	agx::AutoInit agxInit;
	// 実行する経路情報のファイルパスを入力
	std::cout << "実行するファイルのパスを入力" << std::endl;
	string filePath;
	cin >> filePath;
	filePath = "c:\\Users\\hayashi\\Desktop\\stringRoute\\modify\\" + filePath;
	std::cout << filePath << std::endl;
	nodePosition = readFile(filePath);

	try {
		agxOSG::ExampleApplicationRef application = new agxOSG::ExampleApplication;
		application->addScene(buildCylinder, '1');
		//application->addScene(buildWire, '2');

		if (application->init(argc, argv)) {
			return application->run();

		}
	}
	catch (std::exception& e) {
		std::cerr << "\nCaught exception: " << e.what() << std::endl;
		return 1;
	}
	return 0;
}