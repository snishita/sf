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

agx::RigidBodyRef cylL[5]; // �����̍��̂��i�[
agx::RigidBodyRef cylR[5]; // �E���̍��̂��i�[
agx::Vec3 wireNodePosition[];	// ���C���[��Node(�����_)���i�[
vector<float> nodePosition;	// �o�H���̃t�@�C������擾����Node�̍��W�l���i�[
vector<agx::Vec3> outputNodePos; // �o�͎���Wire��Node���i�[
agxWire::Wire* wire; // �o�H���ɏ]���\�����郏�C���[
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

// ��؂蕶������菜��
vector<string> split(string& input, char delimiter = ',')
{
	istringstream stream(input);
	string field;
	vector<string> result;
	size_t c;

	// ��������R���}<,>��؂�
	while (getline(stream, field, delimiter)) {
		// ����< [ >�ƃX�y�[�X< >���폜
		while ((c = field.find_first_of("[ ")) != string::npos) {
			field.erase(c, 1);
		}
		// ����< ] >�ƃX�y�[�X< >���폜
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

// ���W�l�ȊO�̏��Ȃ�true
// ���������Ȃ̂ł��Ƃŏ���������
bool checkLR(std::string check) {
	bool ans = false;
	if (check == "LT" || check == "LF" || check == "LM" || check == "LR" || check == "LL" ||
		check == "RT" || check == "RF" || check == "RM" || check == "RR" || check == "RL") {
		ans = true;
	}
	return ans;

}

// txt�t�@�C������o�H���̓ǂݍ���
// �����Ɏ��s����o�H���̃e�L�X�g�t�@�C��
vector<float> readFile(const string fileName) {
	std::ifstream ifs(fileName);
	std::string file;

	vector<float> position;

	// ifs�̕������1�s����file��
	while (getline(ifs, file)) {
		//�@�J���}�Ȃǂ̕s�v�ȕ�������菜��
		vector<string> strvec = split(file);
		// vector�̗v�f�����W�l�ȊO�Ȃ玟�̃��[�v
		if (checkLR(strvec.at(0))) {
			continue;
		}

		// ���W�l��Vector�ɑ��
		int sz = strvec.size();
		if (sz > 3) {
			sz = 3;
		}
		//for (int i = 0; i < strvec.size(); i++) {
		for (int i = 0; i < sz; i++) {
			// String����Float�ɕϊ�
			position.push_back(std::stof(strvec.at(i)));
		}

	}
	std::cout << position.at(2) << endl;
	return position;
}

// Wire�̑S�Ă�Node���擾
// ��Œ��g�̃R�����g�c��
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

// �o�H�����o��
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


// EventListener�̐ݒ�
class KeyboardControl : public agxSDK::GuiEventListener {
public:
	// �����ɑ��삷�鍄�̂̔z��
	KeyboardControl(agx::RigidBodyRef* LRigidBody, agx::RigidBodyRef* RRigidBody)
		:lBody(LRigidBody), rBody(RRigidBody)
	{
		// We only want to listen to keyboard events.
		setMask(agxSDK::GuiEventListener::KEYBOARD);
	}


	virtual bool keyboard(int key, unsigned int modKeyMask, float /*x*/, float /*y*/, bool keydown)
	{

		bool handled = false;
		double x_velocity = 0;				// x���̑��x
		double y_little_thumb_finger = 0;	// ���w�Ɛe�w��y���̑��x
		double y_index_ring_finger = 0;		// ��w�Ɛl�����w��y���̑��x
		double initialized = 10;


		if (!lBody->isValid()) {
			return false;
		}

		// ���E�̍��̂�x���ɋ��߂�
		if (key == agxSDK::GuiEventListener::KEY_Left) {
			x_velocity = -initialized;
			y_little_thumb_finger = 0;
			y_index_ring_finger = 0;

			handled = true;

		}
		// ���E�̍��̂�x���ɍL����
		else if (key == agxSDK::GuiEventListener::KEY_Right) {
			x_velocity = initialized;
			y_little_thumb_finger = 0;
			y_index_ring_finger = 0;

			std::cout << "�L����" << endl;

			handled = true;
		}
		// ���̂�y���ɍL����
		else if (key == agxSDK::GuiEventListener::KEY_Up) {
			x_velocity = initialized;
			y_little_thumb_finger = initialized;
			y_index_ring_finger = initialized / 2.0;

			handled = true;
		}
		// ���̂�y���ɋ��߂�
		else if (key == agxSDK::GuiEventListener::KEY_Down) {
			x_velocity = 0;
			y_little_thumb_finger = -initialized;
			y_index_ring_finger = -initialized / 2.0;

			handled = true;
		}
		// ���̂̓�����~
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

			std::cout << "�o�͂���t�@�C���p�X�����" << endl;
			string filePath;
			cin >> filePath;
			// ���͗ʂ����炷����syuusei�܂ł̃p�X���w��
			filePath = "c:\\Users\\hayashi\\Desktop\\stringRoute\\output\\" + filePath;
			outputNodeRoute(filePath);
		}
		else if (key == agxSDK::GuiEventListener::KEY_Shift_L) {
			rerunTest = true;
			string filePath;
			cin >> filePath;
		}

		// ���̂ɑ��x��ݒ�
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

	// �Č����s�����Ԃ�ݒ�
	simulation->agxSDK::Simulation::setTimeStep(1.0 / 7000.0);

	// �Č���ԓ��̏d�͂�ݒ�
	agx::Vec3 gravity = agx::Vec3(0, 0, 0);
	simulation->setUniformGravity(gravity);


	// �J�����̈ʒu���w��
	agx::Vec3 eye = agx::Vec3(0, 0, 5.5);
	agx::Vec3 center = agx::Vec3(0, 0, 0);
	agx::Vec3 up = agx::Vec3(0, -1, 0);
	application->setCameraHome(eye, center, up);

	// Create a static box that will hold the end of each wire.
	double cylinderPos = -0.9; // ���w�̍��̂̏������W
	double space = 0.45;	   // ���̓��m�̐����Ԋu

	double x = 0.3;
	// ���w�`�e�w�̏��ɉ~���𐶐�
	for (int i = 0; i < sizeof(cylR) / sizeof(cylR[0]); i++) {
		// �����̉~���𐶐�
		cylL[i] = new agx::RigidBody(new agxCollide::Geometry(new agxCollide::Cylinder(0.08, 2.5)));
		//cylL[i]->setPosition(0.9 + x, cylinderPos, 0); //x�̒l��+-0.9����q���������L�΂����l�����Z����
		cylL[i]->setPosition(nodePosition.at(2) + x -0.05, cylinderPos, 0); //x�̒l��+-0.9����q���������L�΂����l�����Z����
		cylL[i]->setMotionControl(agx::RigidBody::KINEMATICS);
		cylL[i]->setRotation(agx::Quat::rotate(agx::Vec3::Y_AXIS(), agx::Vec3::Z_AXIS()));
		agxOSG::setDiffuseColor(agxOSG::createVisual(cylL[i], root), agxRender::Color::PaleGoldenrod());
		simulation->add(cylL[i]);

		// �E���̉~���𐶐�
		cylR[i] = new agx::RigidBody(new agxCollide::Geometry(new agxCollide::Cylinder(0.08, 2.5)));
		//cylR[i]->setPosition(-0.9 - x, cylinderPos, 0);	//x�̒l��+-0.9����q���������L�΂����l�����Z����
		cylR[i]->setPosition(-nodePosition.at(2) - x + 0.05, cylinderPos, 0);	//x�̒l��+-0.9����q���������L�΂����l�����Z����
		cylR[i]->setMotionControl(agx::RigidBody::KINEMATICS);
		cylR[i]->setRotation(agx::Quat::rotate(agx::Vec3::Y_AXIS(), agx::Vec3::Z_AXIS()));
		agxOSG::setDiffuseColor(agxOSG::createVisual(cylR[i], root), agxRender::Color::LightGoldenrodYellow());
		simulation->add(cylR[i]);

		// ���ɐ�������ʒu�����炷
		cylinderPos += space;
	}

	// ���̂�EventListener��ݒ�
	KeyboardControl* keyboard = new KeyboardControl(cylR, cylL);
	simulation->addEventListener(keyboard);


	// ���C���[�̒[��ڑ����邽�߂̍���
	agx::RigidBodyRef connectWireRigidBody;
	connectWireRigidBody = new agx::RigidBody(new agxCollide::Geometry(new agxCollide::Box(0.01, 0.01, 0.01)));
	connectWireRigidBody->setPosition(nodePosition.at(3), nodePosition.at(4), nodePosition.at(5));
	simulation->add(connectWireRigidBody);
	agxOSG::createVisual(connectWireRigidBody, root);

	// wire���f���̐���
	double wireRadius = 0.01;	// ���C���[�̔��a
	int wireResolutin = 1;		// ���C���[�̕����Ԋu

	wire = new agxWire::Wire(wireRadius, wireResolutin, true);
	
	// ���̂ɐڑ��B�q���̍ŏ��ƍŌ�̃m�[�h����x�N�g�������߂āA�ڑ��ʒu������
	int sz = nodePosition.size();
	agx::Vec3 rt = agx::Vec3(nodePosition.at(6)-nodePosition.at(sz-3), nodePosition.at(7)-nodePosition.at(sz-2), nodePosition.at(8)-nodePosition.at(sz-1));
	rt = rt / rt.length() * 0.01;
	wire->add(new agxWire::BodyFixedNode(connectWireRigidBody, rt));	// ���̂ɐڑ�

	// �o�H���ɉ������t���[�m�[�h�̍쐬
	for (int i = 6; i < nodePosition.size(); i += 3) {
		wire->add(new agxWire::FreeNode(nodePosition.at(i), nodePosition.at(i + 1), nodePosition.at(i + 2)));
	}

	wire->add(new agxWire::BodyFixedNode(connectWireRigidBody, rt*(-1)));	// ���C���[�̔��Α������̂ɐڑ�
	simulation->add(wire);

	// ���C���[���m�̏Փ˔���
	agxWire::WireController::instance()->setEnableCollisions(wire, wire, true);


	agxOSG::WireRendererRef wireRenderer = new agxOSG::WireRenderer(wire, root);
	wireRenderer->setColor(agxRender::Color::GreenYellow());
	simulation->add(wireRenderer);

	return root;
}



// ���C���̎��s��
int main(int argc, char** argv)
{
	agx::AutoInit agxInit;
	// ���s����o�H���̃t�@�C���p�X�����
	std::cout << "���s����t�@�C���̃p�X�����" << std::endl;
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