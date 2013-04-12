
class monitorcache_router(object):

    def db_for_read(self, model, **hints):
   
        if model._meta.app_label == 'monitorcache':
            return 'monitorcache'
        return None

    def db_for_write(self, model, **hints):
    
        if model._meta.app_label == 'monitorcache':
            return 'monitorcache'
        return None

    def allow_relation(self, obj1, obj2, **hints):
    
        if obj1._meta.app_label == 'monitorcache' or \
           obj2._meta.app_label == 'monitorcache':
           return True
        return None

    def allow_syncdb(self, db, model):
     
        if db == 'monitorcache':
            return model._meta.app_label == 'monitorcache'
        elif model._meta.app_label == 'monitorcache':
            return False
        return None
