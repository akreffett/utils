import maec_bundle_3_0 as maecbundle
import cybox.port_object_1_3 as cybox_port_object

class port_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, port_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.id, type_="Port")
        portobj = self.port_from_dict(port_attributes)
                
        for key, value in port_attributes.items():
            if key == 'association':
                cybox_object.set_association_type(value)
                
        if portobj.hasContent_():
            cybox_object.set_Defined_Object(portobj)
        
        return cybox_object
    
    @classmethod
    def cybox_port_from_dict(self, port_attributes):
        portobj = cybox_port_object.PortObjectType()
        portobj.set_anyAttributes_({'xsi:type' : 'PortObj:PortObjectType'})
        for key, value in port_attributes.items():
            if key == 'port_value' and self.__value_test(value):
                portobj.set_Port_Value(maecbundle.cybox_common_types_1_0.PositiveIntegerObjectAttributeType(datatype='PositiveInteger', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'protocol' and self.__value_test(value):
                if value == 'tcp':
                    portobj.set_Layer4_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='TCP'))
                elif value == 'udp':
                    portobj.set_Layer4_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='UDP'))
                
        return portobj