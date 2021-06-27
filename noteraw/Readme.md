# 聲明
   * 此筆記有出現的程式碼皆為參考鐘誠老師
# Week1
* 這門課基本上會使用現成的模型(因為算力不夠)
* 使用python + PyTorch(學術界偏好)
* python 會用到Numpy Scipy mataplot pandas
## 人工智慧
* 傳統
   * 搜尋(解空間搜尋) + 優化
* 機器學習
   * 統計
   * 神經網路-深度學習 (CNN RNN LSM EERT)
* 應用
   * 影像
      * 辨識 
      * CNN yolo
   * 語言
      * 規則
      * RNN BERT
   * 下棋
      * MKTS    
   * 自動控制
      * 機器人/車
* 人工智慧的大議題-落地(人類學家)
   * 該如何將這些理論實際應用在人的生活中(考量各種成本)
   * UX
   * 像是alpha go 下棋下很強但實際上有什麼效益呢? 不知道...可能是頂尖棋手獲得挫折感
* 數學(優化) 期中小考可能會考這些數學
   * 微積分(偏微分 連鎖率)
   * 代數
      * 線代
      * 泛函分析
   * 幾何
      * 微分幾何ㄏ
   * 機率統計
## 爬山演算法
單變數(二維) 和雙變數(三維)介紹
深度學習用到幾萬維甚至幾億維
可惜人腦通常到三維就極限了 四維很難去想像，所以只能交給機器來搞
# Week2
* 講解演算法hillclimbing1 hillclimbing2
 * 往高處爬，只要旁邊比較高，就移動到旁邊
 * 只能找到局部最佳解(可能旁邊低，但是旁邊的旁邊更高)，找不到全域最佳解
* 模擬退火法
```
Algorithm SimulatedAnnealing(s)
  while (溫度還不夠低，或還可以找到比 s 更好的解 s' 的時候)
    根據能量差與溫度，用機率的方式決定是否要移動到新解 s'。
    # (機率：溫度高時可以往上走，溫度低的時候差不多只能往下走)
    將溫度降低一些
  end
end
```
# Week3
* 講解遺傳演算法
   * 分數最高跟最低選到的機率相差兩倍
   * 問題的表達式的特性應該:好的基因跟好的基因組合起來得到更好的機會應該要比較大
   * 遺傳演算法跑的速度很慢
* 加密
   * 凱撒密碼
       * 是一種替換加密技術，明文中的所有字母都在字母表上向後（或向前）按照一個固定數目進行偏移後被替換成密文
       * 假如原本的訊息是 'attackatdawn' 那麼在英文字母順序位移到下一個字，例如 a 變 b，b 變 c 的編碼之下， 訊息就成了 'bubdlbuebxo'
   * 維吉尼亞密碼
      * 維吉尼亞密碼是凱薩密碼的進化版，其方法是將位移量從單一數字變成一連串的位移，讓金鑰變成金鑰陣列
      * 舉例而言，假如用 0 2 4 當位移，那麼 attackatdawn這句話編碼後，會變成 avxaemavhwp 這個句子
 ```
    a + 0 = a
    t + 2 = v
    t + 4 = x
    a + 0 = a
    c + 2 = e
    k + 4 = m
    a + 0 = a
    t + 2 = v
    d + 4 = h
    w + 0 = w
    n + 2 = p
```
* XOR 密碼
   * XOR 是二進位運算中的基本邏輯閘，當兩個位元相同時就輸出 0，不相同時就輸出 1
   * 解密的好處是當我們對某位元連續與某樣式位元連續作兩次 XOR 運算時，就會得到原來的位元
   * 例:M XOR K XOR K = M，只要用金鑰K對某訊息作XOR運算之後就可以得到密文 C，然後再用K對密文C作一次XOR運算又可以得到原來的M訊息。
```
原始訊息：11101110 00000111 10000001 11000001
加密金鑰：10101111 10101111 10101111 10101111  
---------------------------------------------- (第一次 XOR 加密)
密文訊息：01000001 10101000 00101110 01101110
加密金鑰：10101111 10101111 10101111 10101111  
---------------------------------------------- (第二次 XOR 解密)
解密訊息：11101110 00000111 10000001 11000001
```
## 參考資料
* [加密](https://zh.wikipedia.org/wiki/%E5%8A%A0%E5%AF%86)
* [凱薩密碼](https://zh.wikipedia.org/wiki/%E5%87%B1%E6%92%92%E5%AF%86%E7%A2%BC)
# Week4
* 遺傳演算法 
   * 父親母親混一半 
   * 能夠獲得更好的解才會適合使用
* 線性規劃 linearprogramming1.py 
   * 高中學過 高中的解法是 先把範圍框起來然後將交點(函數可以作圖)帶入函數
* 整數規劃(較難，NP完全) 
   
* NP完全
    * 可參考 https://www.ycc.idv.tw/algorithm-complexity-theory.html

* SAT 給布林式 找出她的解
    * Satisfiability
    * 是用來解決給定的真值方程式
    第一個被證明屬於NP完全的問題
* 表達graph 
    * 相鄰矩陣 
    * 相鄰串列 
    * 字典等來表達
# Week5
* permutation  truethable queen
   * 老師建議 先把前兩個搞懂 會比較容易懂queen
* 八皇后
   * 在8x8的棋盤上放置8個皇后，任意1個皇后的橫豎兩條對角線座標都不能有皇后
# Week6
* 介紹數學 可以參考week1 的架構 及老師的slide
* 能把學過的數學寫成程式 可以證明 這個東西你真的會!!
[用十分鐘快速掌握《數學的整體結構》](https://www.slideshare.net/ccckmit/ss-68579935)
# Week8
* chess
* 圍棋是最難的棋，alphago在圍棋打敗棋王 代表-->所有的棋 電腦都能稱霸
# Week9
* 神經網路
   * 人工神經網路，簡稱神經網路或類神經網路，在機器學習和認知科學領域，是一種模仿生物神經網路的結構和功能的數學模型或計算模型，用於對函式進行估計或近似
   * 大多數情況下人工神經網路能在外界資訊的基礎上改變內部結構，是一種自適應系統，通俗地講就是具備學習功能

* 複習微分觀念 geadient gd
   * 微分 其實就是找切線斜率

## 單變數微分
### diff
* code
```
def f(x):
    # return x*x
    return x**3

dx = 0.001 /求逼近

def diff(f, x):
    df = f(x+dx)-f(x)
    return df/dx

print('diff(f,2)=', diff(f, 2))
```
* 執行結果
```
$ python diff.py
diff(f,2)= 12.006000999997823
```
### e (自然常數、自然底數)
* e的微分是自己，積分也是自己
* 執行結果會趨近於e
* code
```
def e(n):
	return (1+1.0/n)**n

for i in range(100):
	n = (i+1)*100.0
	print('n=', n, 'e(n)=', e(n))
```
* 執行結果
```
$ python e.py
n= 100.0 e(n)= 2.7048138294215285
n= 200.0 e(n)= 2.711517122929317
n= 300.0 e(n)= 2.7137651579427837
n= 400.0 e(n)= 2.7148917443812293
n= 500.0 e(n)= 2.715568520651728
n= 600.0 e(n)= 2.7160200488806514
n= 700.0 e(n)= 2.7163427377295566
n= 800.0 e(n)= 2.716584846682471
n= 900.0 e(n)= 2.716773208380411
n= 1000.0 e(n)= 2.7169239322355936
n= 1100.0 e(n)= 2.717047274569425
.
.
.
n= 8600.0 e(n)= 2.71812380566317
n= 8700.0 e(n)= 2.7181256218249055
n= 8800.0 e(n)= 2.718127396711982
n= 8900.0 e(n)= 2.718129131725891
n= 9000.0 e(n)= 2.7181308281830128
n= 9100.0 e(n)= 2.718132487359168
n= 9200.0 e(n)= 2.718134110467929
n= 9300.0 e(n)= 2.718135698675662
n= 9400.0 e(n)= 2.718137253097062
n= 9500.0 e(n)= 2.7181387748001744
n= 9600.0 e(n)= 2.718140264795318
n= 9700.0 e(n)= 2.718141724076723
n= 9800.0 e(n)= 2.718143153583405
n= 9900.0 e(n)= 2.718144554210053
n= 10000.0 e(n)= 2.7181459268249255
```

* 梯度下降
   * 跟爬山演算法有點像
   * 一直網斜率最大的地方走
   * 有可能卡在局部最低點
# Week10
* 04logic kb
* prolog
   * 邏輯編程
   * 最基本的寫法是定義物件與物件之間的關係

* 介紹一些數學悖論 
   * 羅素悖論 
      * 理髮師只為不替自己替鬍子的人剃鬍子
      * 那他替自己的鬍子嗎? 
   * 飛矢不動 
   * 跑得快的永遠追不上跑得慢的
      * 因為跑得快原本就在跑得慢的的前面，所以永遠追不到
# Week11
* 05-01 numpy matplotlib curve1 curve2 curve3d
   * numbpy支援高維度陣列的運算
   * 用numpy來操作矩陣會比python的內建含式庫快
* sympy derive1 dintergtate1 factor1 limit1 plot(較少用) simplify1 solve1 solve2 solveRoot2 sqrt1 sym1
   * SymPy是一個符號計算的Python庫
* 05-03 algebra root2 
* matrix determinent1 (複習高師消去 矩陣運算) detLU detTerorem1 detTheorem2 eigen1 matrix1 matrix2 solve1 svd1
type complex
* 05-04 chaos 
   * 碎形，又稱分形、殘形，通常被定義為「一個粗糙或零碎的幾何形狀，可以分成數個部分，且每一部分都（至少近似地）是整體縮小後的形狀」
   * 碎形在數學中是一種抽象的物體，用於描述自然界中存在的事物。
   * 人工碎形通常在放大後能展現出相似的形狀
* lorenz 
   * 勞侖次吸引子（Lorenz attractor）是勞侖次振子（Lorenz oscillator）的長期行為對應的碎形結構
   * 勞侖次振子是能產生混沌流的三維動力系統，又稱作勞侖次系統（Lorenz system），其一組混沌解稱作勞侖次吸引子，以其雙紐線形狀而著稱
   * 映射展示出動力系統（三維系統的三個變量）的狀態是如何以一種複雜且不重複的模式，隨時間的推移而演變的
* diffequation diffeq1 diffeqRC
* fourier 01 (keyword:傅立葉轉換 傅立葉級數 傅立葉分析) 
   * [沒有數學的傅立葉](https://kknews.cc/zh-tw/education/p6qjkxp.html)
* jpeg 破壞性圖像格式(將原圖檔案變小但肉眼看不太出來根原圖有什麼差別)
# Week12
* 語言處理 10lang rule e2c 03gen
* 04 gen_math 
* 04b textgen
* 老師的 語言處理技術 slide
* 06 jieba
* 07 opencc
# Week13
* 梯度下降 反傳遞 
   * 讓梯度下降可以透過目前的值來決定下一個鄰近點的大小
   * ex:1m走了10步 數值沒有變動 我們可能會讓他變成2公尺為最小單位
* 07-03 net1
* 07-04 torch autograd0 autograd1 autograd2
   * torch 一個以自動微分為基礎的函式庫
* 07-05 torchGd1 tochGd2 torchGd3
* 07-06 regression1 regression2
* 07-06-example 
# Week14
* 人工智慧的方法
   * 比對法
      * 紀錄問題與答案配對後，直接從表格內查出。
    * 推理法
      * 撰寫規則後，電腦根據規則推論。
   * 搜尋法
      * 對所有可能的結果進行系統式的列舉，然後看看有沒有答案。
   * 統計法
      * 找出機率最大的解答。
   * 優化法
      * 對每個可能的解答，都給一個分數及權重，找出總分最好的解答。
* 深度學習的神經網路

   * [循環神經網路RNN, LSTM](https://brohrer.mcknote.com/zh-Hant/how_machine_learning_works/how_rnns_lstm_work.html)
   * [生成對抗網路GAN](https://medium.com/@hiskio/%E7%94%9F%E6%88%90%E5%B0%8D%E6%8A%97%E7%B6%B2%E8%B7%AF%E5%88%B0%E5%BA%95%E5%9C%A8gan%E9%BA%BB-f149efb9eb6b)
   * [Reinforcement Learning](https://taweihuang.hpd.io/2016/09/16/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E8%88%87%E5%A2%9E%E5%BC%B7%E5%AD%B8%E7%BF%92-1%EF%BC%9A%E4%BB%80%E9%BA%BC%E6%98%AF%E5%A2%9E%E5%BC%B7%E5%AD%B8%E7%BF%92%EF%BC%9F/)
# Week15
* Colab
   * google的一款產品
   * pros
      * 免費高規格的GPU
      * 不占電腦內部空間
      * 可以多開coalab
   * cons
      * 要有穩定的網路
      * 判定閒置的話會被關掉
      * 有時間限制(畢竟免費阿)
* [RNN LSTM One-hot Encoding](https://brohrer.mcknote.com/zh-Hant/how_machine_learning_works/how_rnns_lstm_work.html)
# Week16
* 人工智慧>機器學習>深度學習
* [最大概似估計](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E4%BC%BC%E7%84%B6%E4%BC%B0%E8%AE%A1)
* [蒙地卡羅方法 (Monte Carlo method)](https://zh.wikipedia.org/wiki/%E8%92%99%E5%9C%B0%E5%8D%A1%E7%BE%85%E6%96%B9%E6%B3%95)
* [黎曼積分](https://zh.wikipedia.org/wiki/%E9%BB%8E%E6%9B%BC%E7%A7%AF%E5%88%86)
* [馬可夫鏈 (Markov chain)](https://zh.wikipedia.org/zh-tw/%E9%A9%AC%E5%B0%94%E5%8F%AF%E5%A4%AB%E9%93%BE)
* [隱藏式馬可夫模型(Hidden Markov Model)](https://zh.wikipedia.org/wiki/%E9%9A%90%E9%A9%AC%E5%B0%94%E5%8F%AF%E5%A4%AB%E6%A8%A1%E5%9E%8B)
* [維特比演算法（Viterbi algorithm）](https://zh.wikipedia.org/zh-tw/%E7%BB%B4%E7%89%B9%E6%AF%94%E7%AE%97%E6%B3%95)
* [最大期望演算法 （Expectation-maximization algorithm)](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E6%9C%9F%E6%9C%9B%E7%AE%97%E6%B3%95)
* [K-近鄰演算法](https://zh.wikipedia.org/wiki/K-%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95)
* [決策樹(Decision Tree)](https://zh.wikipedia.org/wiki/%E5%86%B3%E7%AD%96%E6%A0%91)
* [隨機森林(Random Forest)](https://zh.wikipedia.org/wiki/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97)
* [支援向量機 Support Vector Machine (SVM)](https://zh.wikipedia.org/wiki/%E6%94%AF%E6%8C%81%E5%90%91%E9%87%8F%E6%9C%BA)
# Week17
* [中央極限定理](https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%BF%83%E6%9E%81%E9%99%90%E5%AE%9A%E7%90%86)
   * 中央極限定理是機率論中的一組定理
   * 在適當的條件下，大量相互獨立隨機變數的均值經適當標準化後依分布收斂於常態分布
   * 這組定理是數理統計學和誤差分析的理論基礎，指出了大量隨機變數之和近似服從常態分布的條件\
![PICTURE](https://github.com/mark456tung/ai109b/blob/main/noteraw/CLT.png)
* 圖片轉自維基
* googlemt1.py
   * [使用 googletrans 套件來進行 Google 翻譯](https://clay-atlas.com/blog/2020/05/05/python-cn-note-package-googletrans-google-translate/)
   * `pip install googletrans`
* [使用 Gensim 套件將文字轉成向量](https://clay-atlas.com/blog/2020/01/17/python-chinese-tutorial-gensim-word2vec/)
   * `pip install gensim`
# Week18
## 鍾誠老師上課教材
* [程式人媒體_人工智慧](https://programmermedia.org/root/%E7%A8%8B%E5%BC%8F%E4%BA%BA%E5%AA%92%E9%AB%94/)
## 台大人工智慧學習連結
* [台大李宏毅老師的課程](http://speech.ee.ntu.edu.tw/~tlkagk/courses_DLHLP20.html)
* [台大林軒田老師的課程](https://www.csie.ntu.edu.tw/~htlin/course/ml20fall/)
## 李永樂老師的YT教學
* [機器能像人一樣思考嗎？人工智能（一）機器學習和神經網絡](https://www.youtube.com/watch?v=5A9bmW1qTpk)
* [人工智能是怎么学习的？](https://www.youtube.com/watch?v=FrunoBR37c4)
## 線上學習資源
* [莫煩python](https://mofanpy.com/)
* [Udemy](https://www.udemy.com/)
* [Coursera](https://www.coursera.org/)
## 電子書
* [Deep Learning An MIT Press book](https://www.deeplearningbook.org/)
* Google : Deep Learning 書 github
* [《动手学深度学习》](https://github.com/MingchaoZhu/DeepLearning)
* [深度学习 AI圣经(Deep Learning)](https://github.com/MingchaoZhu/DeepLearning)

 [License](https://github.com/mark456tung/ai109b/blob/main/LICENSE.md)