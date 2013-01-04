import maec_bundle_3_0 as maecbundle
import cybox.address_object_1_2 as cybox_address_object

class address_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, address_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_="IP Address")
        addr_object = self.cybox_address_from_dict(address_attributes)
        
        for key, value in address_attributes.items():
            if key == 'related_objects':
                related_objects = maecbundle.cybox_core_1_0.RelatedObjectsType()
                for related_object in value:
                    related_objects.add_Related_Object(related_object)
                if related_objects.hasContent_():
                    cybox_object.set_Related_Objects(related_objects)
            elif key == 'association' and self.__value_test(value):
                cybox_object.set_association_type(value)
        
        if addr_object.hasContent_():
            cybox_object.set_Defined_Object(addr_object)
        
        return cybox_object
    
    @classmethod
    def cybox_address_from_dict(self, address_attributes):
        addrobject = cybox_address_object.AddressObjectType()
        addrobject.set_anyAttributes_({'xsi:type' : 'AddressObj:AddressObjectType'})
        
        for key, value in address_attributes.items():
            if key == 'category' and self.__value_test(value):
                addrobject.set_category(value)
            elif key == 'ext_category' and self.__value_test(value):
                addrobject.set_Ext_Category(value)
            elif key == 'vlan_name' and self.__value_test(value):
                addrobject.set_VLAN_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'vlan_num' and self.__value_test(value):
                addrobject.set_VLAN_Num(maecbundle.cybox_common_types_1_0.IntegerObjectAttributeType(datatype='Integer', valueOf_=maecbundle.quote_xml(value)))
            # TODO: implement Is_Source and Is_Destination for AddressObject
            #elif key == 'is_source':
            #    if self.__value_test(value):
            #        addrobject.set_Is_Source(value?true:false)
            #elif key == 'is_destination':
            #    if self.__value_test(value):
            #        addrobject.set_Is_Destination(value?true:false)
            elif key == 'address_value' and self.__value_test(value):
                addrobject.set_Address_Value(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            
        return 