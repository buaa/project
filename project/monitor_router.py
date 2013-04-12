class monitor_router(object):

    def db_for_read(self, model, **hints):
   
        if model._meta.app_label == 'monitor':
            return 'monitor'
        return None

    def db_for_write(self, model, **hints):
    
        if model._meta.app_label == 'monitor':
            return 'monitor'
        return None

    def allow_relation(self, obj1, obj2, **hints):
    
        if obj1._meta.app_label == 'monitor' or \
           obj2._meta.app_label == 'monitor':
           return True
        return None

    def allow_syncdb(self, db, model):
     
        if db == 'monitor':
            return model._meta.app_label == 'monitor'
        elif model._meta.app_label == 'monitor':
            return False
        return None
