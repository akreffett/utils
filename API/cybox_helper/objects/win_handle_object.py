import maec_bundle_3_0 as maecbundle
import cybox.win_handle_object_1_3 as cybox_win_handle_object

class win_handle_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, handle_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Handle')
        handle_obj = cybox_win_handle_object.WindowsHandleObjectType()
        handle_obj.set_anyAttributes_({'xsi:type' : 'WinHandleObj:WindowsHandleObjectType'})
        
        for key, value in handle_attributes.items():
            if key == 'id' and self.__value_test(value):
                handle_obj.set_ID(maecbundle.cybox_common_types_1_0.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt', valueOf_=value))
            if key == 'type' and self.__value_test(value):
                handle_obj.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if handle_obj.hasContent_():
            cybox_object.set_Defined_Object(handle_obj)
        
        return cybox_object