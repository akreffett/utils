import maec_bundle_3_0 as maecbundle
import cybox.uri_object_1_2 as cybox_uri_object

class internet_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, internet_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='URI')
        uriobj = cybox_uri_object.URIObjectType()
        uriobj.set_anyAttributes_({'xsi:type' : 'URIObj:URIObjectType'})
        #set object attributes
        for key, value in internet_attributes.items():
            if key == 'uri' and self.__value_test(value):
                uriobj.set_Value(maecbundle.cybox_common_types_1_0.AnyURIObjectAttributeType(datatype='AnyURI', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'association':
                cybox_object.set_association_type(value)
                
        if uriobj.hasContent_():
            cybox_object.set_Defined_Object(uriobj)
            
        return cybox_object