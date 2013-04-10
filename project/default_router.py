class default_router(object):

    def db_for_read(self, model, **hints):
   
        if model._meta.app_label == 'default':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
    
        if model._meta.app_label == 'default':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
    
        if obj1._meta.app_label == 'default' or \
           obj2._meta.app_label == 'default':
           return True
        return None

    def allow_syncdb(self, db, model):
     
        if db == 'default':
            return model._meta.app_label == 'default'
        elif model._meta.app_label == 'default':
            return False
        return None