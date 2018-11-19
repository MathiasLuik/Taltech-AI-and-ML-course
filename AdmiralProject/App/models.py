from django.db import models

class Node(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return "(id: %s, parent: %s, name: %s)" % (self.id, self.parent, self.name)
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
            #"parent": self.parent
        }
    def get_parent(self):
        return {
            "parent": self.parent    
        }