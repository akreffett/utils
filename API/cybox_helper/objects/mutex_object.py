import maec_bundle_3_0 as maecbundle
import cybox.win_mutex_object_1_2 as cybox_win_mutex_object

class mutex_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, mutex_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Mutex')
        mutex_obj = cybox_win_mutex_object.WindowsMutexObjectType()
        mutex_obj.set_anyAttributes_({'xsi:type' : 'WinMutexObj:WindowsMutexObjectType'})
        
        for key, value in mutex_attributes.items():
            if key == 'name' and self.__value_test(value):
                mutex_obj.set_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
                mutex_obj.set_named(True)
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if mutex_obj.hasContent_():
            cybox_object.set_Defined_Object(mutex_obj)
        
        return cybox_object