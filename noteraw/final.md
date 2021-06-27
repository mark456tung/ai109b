* 前言
   * [此報告的code參考自github上的mc6666](https://github.com/mc6666/Keras_tutorial/blob/master/12_01_CatAndDog.ipynb)
   * 報告的內容為此code用到的觀念(為自己吸收後寫出的解釋)
   * [我加上註解後的程式碼](https://github.com/mark456tung/ai109b/blob/main/noteraw/final12_01_CatAndDog.ipynb)
   * AI好難
* CNN卷積神經網路 
   * 模仿人類的認知方式 把一些特徵數值化 然後逐步堆疊綜合比對就可以得到比較好的辨識結果
   * 典型的CNN作法是多層卷積/池化後，萃取特徵當作 Input，再接至一到多個完全連接層，進行分類。
![image](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-07-at-4-59-29-pm.png?w=748)
[圖片來源](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/)

   * 卷積層
      * input 5x5 image的輸出成3x3的特徵的過程
      * ![image](https://media.giphy.com/media/i4NjAwytgIRDW/giphy.gif)
     [圖片來源GIPHY 是一個無版權的素材網站](https://giphy.com/gifs/blog-daniel-keypoints-i4NjAwytgIRDW?utm_source=media-link&utm_medium=landing&utm_campaign=Media%20Links&utm_term=)
   * 池化層
      * 類似卷積層的取樣方法，不過不是權值加總，通常是取最大值(Max-Polling) 
      ![image](https://miro.medium.com/max/500/1*gpkHl16U7ppl4-lBlnAYqw.gif)
      [圖片來源:Convolutional Neural Networks — Part 4: The Pooling and Fully Connected Layer](https://brightonnkomo.medium.com/convolutional-neural-networks-part-4-the-pooling-and-fully-connected-layer-394ec01fb00d)
*  Batch Normalization 
   * 標準化後的數據 更利於機器來學習
   * 作法就是對每一個 mini-batch 都進行正規化到平均值為0、標準差為1的常態分佈
   * [參考](https://www.youtube.com/watch?v=BZh1ltr5Rkg)

* Depthwise Seperable
   * 一開始看的時候一直看不懂通道是什麼...原來我前面理解的是單通道輸入單通道輸出
      * 這是一個三通道一輸出的例子
      * ![](https://pic3.zhimg.com/80/v2-c67c5dab624da0904b34b2cb674ed6d2_720w.jpg)
      * [圖片來源](https://zhuanlan.zhihu.com/p/251068800)
     * 多通道多輸出的時候用這個方法會比較快
        * ex:輸入通道4輸出8，然後我們的卷積層是3x3大小，那麼每個卷基核需要3x3x4個參數，這樣只是一個通道的輸出，8通道的輸出的話共需要3x3x4x8=288個
     * 用 Depthwise Seperable的話
        * 對4個通道分別卷積 (3x3卷積層)
        * 再用一個(1x1x4卷積核)的通道卷積
        * 3x3x4+(1x1x4)x8 =68
        * [可參考youtube這個時間點的圖會更容易理解](https://youtu.be/hGMQDFrmiPE?t=426)
        * [參考](https://blog.csdn.net/weixin_38668159/article/details/80415626)

* activation 
    * 這邊只是為了方便理解隨意設計的函數
    * 當x < 0.5時 y=0 , else, y=x
    * input =[0, 0.4,0.49,0.51,0.8]
    * ouput =[0, 0, 0, 0.51, 0.8]
    * [詳細參考](https://zh.wikipedia.org/wiki/%E6%BF%80%E6%B4%BB%E5%87%BD%E6%95%B0)

* Data Augmentation
  * 是一種用來增加資料集的方法
  * 放大縮小旋轉顛倒，明亮度調整，故意加入噪音等等
 