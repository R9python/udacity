# Dogs VS Cats

## README

* 云平台配置：AWS，实例配置：

  - 12 core CPUs

  - 60G RAM

  - 75G SSD Hard Disk

  - GPU：Tesla P100


    
* 模型准备和搭建、运行时间分两部分：
  - 异常图片清洗：使用了三个预训练模型：Xception：5min, DenseNet201:14min, InceptionResNetV2:15min，小计：34min
  - 模型训练和生成预测结果：Xception:147s, InceptionResNetV2:215s, DenseNet201:177s, train:4min, 小计：12min
  - 以上总计时间：46min
  - 训练时间：只谈train的时间应该是4min
    
