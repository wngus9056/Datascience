import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
import dlib
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import tensorflow.compat.v1 as tf


class MyWindow(QWidget):
    srcFilePath = ""
    styleFilePath = ""
    FaceDector = dlib.get_frontal_face_detector()
    ShapePredictor = dlib.shape_predictor(
        "C:/works/hong_big/beauty/pyQT5_ex/models/shape_predictor_5_face_landmarks.dat"
    )

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(50, 50, 1300, 600)
        self.setWindowTitle("beautyGAN v0.1")
        self.setWindowIcon(QIcon("C:/works/hong_big/beauty/pyQT5_ex/bicon.png"))
    
        # 중간 버튼 레이아웃
        middleLayout = QHBoxLayout()
        self.btnSelect = QPushButton("쌩얼 선택")
        self.btnStyle = QPushButton("스타일 선택")
        self.btnBeauty = QPushButton("Make up")
        self.btnSelect.clicked.connect(self.SelectFile)
        self.btnStyle.clicked.connect(self.SelectStyle)
        self.btnBeauty.clicked.connect(self.MakeupBeauty)
        middleLayout.addWidget(self.btnSelect)
        middleLayout.addWidget(self.btnStyle)
        middleLayout.addWidget(self.btnBeauty)

        # 하단 이미지 및 출력창 레이아웃 전체
        bottomLayout = QHBoxLayout()
        # 하단 왼쪽 이미지 및 출력창 레이아웃
        self.lblImage = QLabel()
        self.lblStyle = QLabel()
        self.matfig = plt.Figure()
        self.canvas = FigureCanvas(self.matfig)
        bottomLayout.addWidget(self.lblImage)
        bottomLayout.addWidget(self.lblStyle)
        bottomLayout.addWidget(self.canvas)

        AllLayout = QVBoxLayout()
        AllLayout.addLayout(middleLayout)
        AllLayout.addLayout(bottomLayout)
        AllLayout.setStretchFactor(bottomLayout, 1)

        self.setLayout(AllLayout)

    def SelectFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Load Image", "")
        if fname:
            self.srcFilePath = fname
            self.qPmSource = QPixmap()
            self.qPmSource.load(fname)
            self.qPmSource = self.qPmSource.scaledToWidth(400)
            self.lblImage.setPixmap(self.qPmSource)

    def SelectStyle(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Load Image", "")
        if fname:
            self.styleFilePath = fname
            self.qPmSource = QPixmap()
            self.qPmSource.load(fname)
            self.qPmSource = self.qPmSource.scaledToWidth(400)
            self.lblStyle.setPixmap(self.qPmSource)

    def align_faces(self, img):
        # 얼굴을 검출한다.
        dets = self.FaceDector(img, 1)
        if len(dets) == 0:
            QMessageBox.information(self, "Message", "사진에서 얼굴을 찾을 수 없습니다!")
            return
        # 객체 검출 모델
        objs = dlib.full_object_detections()

        #검출한 얼굴을 모두 객체 검출 모델로
        for detection in dets:
            s = self.ShapePredictor(img, detection)
            objs.append(s)

        #얼굴을 각도 조절
        faces = dlib.get_face_chips(img, objs, size=256, padding=0.35)
        return faces

    def MakeupBeauty(self):
        # 이미지를 읽어 온다.
        if len(self.srcFilePath) < 2:
            QMessageBox.information(self, "Message", "먼저 원본 사진을 선택 하십시오!")
            return
        # 원본 이미지를 읽는다.
        img1 = dlib.load_rgb_image(self.srcFilePath)
        # 스타일 이미지를 읽는다.
        img2 = dlib.load_rgb_image(self.styleFilePath)

        # img1 은 원본 이미지, img2 는 스타일 이미지
        faces1 = self.align_faces(img1)
        faces2 = self.align_faces(img2)

        src_img = faces1[0]
        ref_img = faces2[0]
        # 얼굴에 대해 전처리 작업을 한다
        X_img = self.preprocess(src_img)
        X_img = np.expand_dims(X_img, axis=0)

        Y_img = self.preprocess(ref_img)
        Y_img = np.expand_dims(Y_img, axis=0)

        with tf.compat.v1.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver = tf.train.import_meta_graph("C:/korAI/pyQT5_ex/models/model.meta")
            saver.restore(sess, tf.train.latest_checkpoint("C:/korAI/pyQT5_ex/models"))
            graph = tf.get_default_graph()
            X = graph.get_tensor_by_name("X:0")
            Y = graph.get_tensor_by_name("Y:0")
            Xs = graph.get_tensor_by_name("generator/xs:0")
            output = sess.run(Xs, feed_dict={X: X_img, Y: Y_img})
            output_img = self.deprocess(output[0])
        # 예측 결과를 matplotlib 에 출력한다.
        ax = self.matfig.add_subplot(111)
        ax.axis("off")
        ax.grid(False)
        ax.imshow(output_img)
        self.canvas.draw()

    def preprocess(self, img):
        return (img / 255.0 - 0.5) * 2

    def deprocess(self, img):
        return (img + 1) / 2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wWindow = MyWindow()
    wWindow.show()
    app.exec_()

