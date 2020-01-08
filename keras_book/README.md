# Keras book (主要是記錄"深度學習密讀:Keras大神帶你用Python實作"這本書的閱讀歷程)

----
## Day1, setup
記錄如何在我的win10環境上安裝Keras的開發環境

### OK版本: 感謝jumbo提供的協助
- 我在win10上安裝anaconda，最初版本是：Anaconda3-2018.12-Windows-x86_64 --> 有來有再更新過，版本…忘了
- 在console下指令，就三行就搞定!：
```
conda create -n cv python=3.7
activate cv
pip install -r requirements.txt
```
- 其中 requirements.txt 的內容為：
```
numpy==1.17.3
matplotlib==3.1.1
Cython==0.29.13
opencv-contrib-python==4.1.1.26
opencv-python==4.1.1.26
h5py==2.10.0
jupyter==1.0.0
pandas==0.25.2
scikit-learn==0.21.3
scipy==1.3.1
seaborn==0.9.0
tensorflow==2.0.0
Keras==2.3.1
```

### NG版本，雖然NG但還是感謝有這些資源可以參考
- 參考這一篇不錯 [link](http://wangwangtc.blogspot.com/2019/06/keras.html)

- 先打開anaconda navigator
- 在enviroments輸入tensorflow，按Create建立一個tensorflow要用的新環境 (跟base分開的)
- 點選「tensorflow」後，在右邊欄選`not installed`，在search輸入keras，選keras，再點下放的apply，就會找到相關套件(keras預設會把tensorflow一起裝)。在清單中再點apply就可以把keras裝好了

- --> 最後在keras的書的ch2的第一個demo這個anaconda的配置就error
- 參考這個看看有沒有解: http://beanobody.blogspot.com/2019/04/module-tensorflow-has-no-attribute.html

----
## CH01
- 簡介Deep Learning的運作方式
- 說明其它ML的技術
    - Naive Bayes theorem
    - logistic regression
    - CNN (Convolutional Neural Network)
    - Kernel methods: 一種分類演算法，最著名的是SVM(Support Vector Machine)，其目標是在找`最初決策邊界`。這是一個少數具備廣泛理論支持，及數學分析的ML演算法。
    - Decision Tree

## CH02
- 以MNIST的實例介紹神經網路的一個範例，並帶出`Class`, `samples`, `label`等名詞的意義
    - 密集層(Dense Layers): fully connected layer, 前後層的神經元全都連在一起
    - loss function: 衡量NN訓練資料的表現，並導正至正確的方向
    - optimizer: 依loss function值而自行更新的機制
    - overfitting
    - tensor
- tensor operations:
    - relu
        - `keras.layers.Dense(512, activation='relu')` --> `output=relu(dot(W, input) + b)`
        - relu(x)即是max(x,0) --> x<0就取0, 反之取x
    - Broadcasting
    - dot
    - reshaping: matrix transposition也是reshaping
- SGD(stochastic gradient descent): 隨機梯度下降，SGD有各種變化，如：momentum SDG, Adagrad, RMSProp

