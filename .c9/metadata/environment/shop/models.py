{"filter":false,"title":"models.py","tooltip":"/shop/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":26},"action":"remove","lines":["from django.db import models","","# Create your models here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":15,"column":28},"action":"insert","lines":["from django.db import models","","# Create your models here.","class Product(models.Model):","    name = models.CharField(max_length=255, blank=False)","    sku = models.CharField(max_length=100, blank=False)","    description = models.TextField(blank=False)","    cost = models.IntegerField(blank=False)","    quantity = models.IntegerField(blank=False, default=0)","    image = models.ImageField(blank=True, null=True)","    ","    def __str__(self):","        return self.name + \" : \" + self.sku","        ","    def getCostInDollars(self):","        return self.cost/100"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":0},"end":{"row":16,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1576430236372,"hash":"173d7ec49ef1049230237e3b8dbf104e76c22e08"}