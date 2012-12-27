#MAEC Analysis Class

#Copyright (c) 2012, The MITRE Corporation
#All rights reserved.

#Compatible with MAEC v3.0
#Last updated 12/27/2012

import maec_package_1_0 as maecpackage
        
class maec_analysis:
    def __init__(self, generator, method = None, type = None, analysis_attributes_dict = None):
        self.generator = generator
        self.analysis = maecpackage.AnalysisType(id=self.generator.generate_ana_id())
        if method is not None:
            self.analysis.set_method(method)
        if type is not None:
            self.analysis.set_type(type)
        self.analysis_attributes_dict = analysis_attributes_dict
        self.tool_list = maecpackage.ToolListType()

    #"Public" methods
    def set_findings_bundle_reference(self, bundle_idref):
        bundle_reference = maecbundle.BundleReferenceType(bundle_idref = bundle_idref)
        self.analysis.set_Findings_Bundle_Reference(bundle_reference)

    def set_summary(self, summary):
        self.analysis.set_Summary(summary)
   
    def add_tool(self, tool_dictionary):
        self.__create_tool(tool_dictionary)

    #Build the Analysis from the input dictionary
    def build_from_dictionary(self):
        for key, value in self.analysis_attributes_dict.items():
            pass

    def get(self):
        if self.tool_list.hasContent_():
            self.analysis.set_Tools(self.tool_list)
        return self.analysis
    
    #"Private" methods

    #Create the MAEC tool type
    def __create_tool(self, tool_dictionary):
        #Create the Tool and set its ID
        tool = maecpackage.cybox_common_types_1_0.ToolInformationType(id=self.generator.generate_tol_id())
        for key, value in tool_dictionary.items():
            if key.lower() == 'description':
                if value is not None and len(value) > 0:
                    tool.set_Description(value)
            elif key.lower() == 'vendor':
                if value is not None and len(value) > 0:
                    tool.set_Vendor(value)
            elif key.lower() == 'name':
                if value is not None and len(value) > 0:
                    tool.set_Name(value)  
            elif key.lower() == 'version':
                if value is not None and len(value) > 0:
                    tool.set_Version(value)
        if tool.hasContent_():
            self.tool_list.add_Tool(tool)
    
    def __build__(self):
        if self.tool_list.hasContent_():
            self.analysis.set_Tools(tool_list)      
