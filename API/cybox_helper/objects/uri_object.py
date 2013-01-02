import maec_bundle_3_0 as maecbundle
import cybox.uri_object_1_2 as cybox_uri_object

class uri_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, uri_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_="URI")
        uriobject = cybox_uri_object.URIObjectType()
        uriobject.set_anyAttributes_({'xsi:type' : 'URIObj:URIObjectType'})
        
        for key, value in uri_attributes.items():
            if key == 'type' and self.__value_test(value):
                uriobject.set_type(value)
            elif key == 'value' and self.__value_test(value):
                uriobject.set_Value(maecbundle.cybox_common_types_1_0.AnyURIObjectAttributeType(datatype='AnyURI', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'related_objects':
                related_objects = maecbundle.cybox_core_1_0.RelatedObjectsType()
                for related_object in value:
                    related_objects.add_Related_Object(related_object)
                if related_objects.hasContent_():
                    cybox_object.set_Related_Objects(related_objects)
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if uriobject.hasContent_():
            cybox_object.set_Defined_Object(uriobject)
        
        return cybox_object