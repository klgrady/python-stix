# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:22 2013 by generateDS.py version 2.9a.
#

import sys
import getopt
import re as re_

import stix.bindings.stix_common as stix_common_binding
import base64
from datetime import datetime, tzinfo, timedelta

XML_NS  = "http://data-marking.mitre.org/Marking-1"

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
# lxml
from lxml import etree as etree_
XMLParser_import_library = XMLParser_import_lxml
if Verbose_import_:
    print("running with lxml.etree")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser(huge_tree=True)
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(tzinfo):
            def __init__(self, offset, name):
                self.__offset = timedelta(minutes = offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node,
                        'Requires sequence of booleans '
                        '("true", "1", "false", "0")')
            return input_data
        def gds_validate_datetime(self, input_data, node, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if isinstance(input_data, basestring):
                return input_data
            if input_data.microsecond == 0:
                _svalue = input_data.strftime('%Y-%m-%dT%H:%M:%S')
            else:
                _svalue = input_data.strftime('%Y-%m-%dT%H:%M:%S.%f')
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_parse_datetime(self, input_data, node, input_name=''):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'GMT')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime.strptime(
                        input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime.strptime(
                        input_data, '%Y-%m-%dT%H:%M:%S')
            return dt.replace(tzinfo = tz)

        def gds_validate_date(self, input_data, node, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = input_data.strftime('%Y-%m-%d')
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_parse_date(self, input_data, node, input_name=''):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'GMT')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            return datetime.strptime(input_data,
                '%Y-%m-%d').replace(tzinfo = tz)
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'utf-8'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (
            msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' %
                (self.name, base64.b64encode(self.value), self.name))
    def to_etree(self, element):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class MarkingType(GeneratedsSuper):
    """MarkingType specifies a structure for marking information to be
    applied to portions of XML content."""
    subclass = None
    superclass = None
    def __init__(self, Marking=None):
        if Marking is None:
            self.Marking = []
        else:
            self.Marking = Marking
    def factory(*args_, **kwargs_):
        if MarkingType.subclass:
            return MarkingType.subclass(*args_, **kwargs_)
        else:
            return MarkingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Marking(self): return self.Marking
    def set_Marking(self, Marking): self.Marking = Marking
    def add_Marking(self, value): self.Marking.append(value)
    def insert_Marking(self, index, value): self.Marking[index] = value
    def hasContent_(self):
        if (
            self.Marking
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='MarkingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MarkingType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='marking:', name_='MarkingType'):
        pass
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='MarkingType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Marking_ in self.Marking:
            Marking_.export(outfile, level, nsmap, namespace_, name_='Marking', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Marking':
            obj_ = MarkingSpecificationType.factory()
            obj_.build(child_)
            self.Marking.append(obj_)
# end class MarkingType


class MarkingStructureType(GeneratedsSuper):
    """The MarkingStructureType contains the marking information to be
    applied to a portion of XML content.This type is defined as
    abstract and is intended to be extended to enable the expression
    of any structured or unstructured data marking mechanism. The
    data marking structure is simply a mechanism for applying
    existing marking systems to nodes. The data marking systems
    themselves define the semantics of what the markings mean, how
    multiple markings to the same node should be applied, and what
    to do if a node is unmarked.It is valid per this specification
    to mark a node with multiple markings from the same system or
    mark a node across multiple marking systems. If a node is marked
    multiple times using the same marking system, that system
    specifies the semantic meaning of multiple markings and (if
    necessary) how conflicts should be resolved. If a node is marked
    across multiple marking systems, each system is considered
    individually applicable. If there are conflicting markings
    across marking systems the behavior is undefined, therefore
    producers should make every effort to ensure documents are
    marked consistently and correctly among all marking systems.STIX
    provides two marking system extensions: Simple, and TLP. Those
    who wish to use another format may do so by defining a new
    extension to this type. The STIX-provided extensions are:1.
    Simple: The Simple marking structures allows for the
    specification of unstructured statements through the use of a
    string field. The type is named SimpleMarkingStructureType and
    is in the http://data-
    marking.mitre.org/extensions/MarkingStructure#Simple-1
    namespace. The extension is defined in the file
    extensions/marking/simple_marking.xsd or at the URL http://stix.
    mitre.org/XMLSchema/extensions/marking/simple_marking/1.1/simple
    _marking.xsd.2. TLP: The TLP marking structure allows for the
    expression of Traffic Light Protocol statements through the use
    of a simple enumeration. The type is named
    TLPMarkingStructureType and is in the http://data-
    marking.mitre.org/extensions/MarkingStructure#TLP-1 namespace.
    The extension is defined in the file
    extensions/marking/tlp_marking.xsd or at the URL http://stix.mit
    re.org/XMLSchema/extensions/marking/tlp/1.1/tlp_marking.xsd.This
    field specifies the name of the marking model to be applied
    within this Marking_Structure.This field contains a reference to
    an authoritative source on the marking model to be applied
    within this Marking_Structure.Specifies a unique ID for this
    Marking_Structure.Specifies a reference to the ID of a
    Marking_Structure defined elsewhere.When idref is specified, the
    id attribute must not be specified, and any instance of this
    Marking_Structure should not hold content."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, marking_model_ref=None, marking_model_name=None):
        self.idref = _cast(None, idref)
        self.marking_model_ref = _cast(None, marking_model_ref)
        self.marking_model_name = _cast(None, marking_model_name)
        self.id = _cast(None, id)
        pass
    def factory(*args_, **kwargs_):
        if MarkingStructureType.subclass:
            return MarkingStructureType.subclass(*args_, **kwargs_)
        else:
            return MarkingStructureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_marking_model_ref(self): return self.marking_model_ref
    def set_marking_model_ref(self, marking_model_ref): self.marking_model_ref = marking_model_ref
    def get_marking_model_name(self): return self.marking_model_name
    def set_marking_model_name(self, marking_model_name): self.marking_model_name = marking_model_name
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='MarkingStructureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MarkingStructureType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='marking:', name_='MarkingStructureType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.marking_model_ref is not None and 'marking_model_ref' not in already_processed:
            already_processed.add('marking_model_ref')
            outfile.write(' marking_model_ref=%s' % (self.gds_format_string(quote_attrib(self.marking_model_ref).encode(ExternalEncoding), input_name='marking_model_ref'), ))
        if self.marking_model_name is not None and 'marking_model_name' not in already_processed:
            already_processed.add('marking_model_name')
            outfile.write(' marking_model_name=%s' % (quote_attrib(self.marking_model_name), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='MarkingStructureType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            self.idref = value
        value = find_attr_value_('marking_model_ref', node)
        if value is not None and 'marking_model_ref' not in already_processed:
            already_processed.add('marking_model_ref')
            self.marking_model_ref = value
        value = find_attr_value_('marking_model_name', node)
        if value is not None and 'marking_model_name' not in already_processed:
            already_processed.add('marking_model_name')
            self.marking_model_name = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class MarkingStructureType


class MarkingSpecificationType(GeneratedsSuper):
    """Specifies a unique ID for this Marking.Specifies a reference to the
    ID of a Marking defined elsewhere.Specifies the relevant
    Data_Marking schema version for this content."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, version=None, Controlled_Structure=None, Marking_Structure=None, Information_Source=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.version = _cast(None, version)
        self.Controlled_Structure = Controlled_Structure
        if Marking_Structure is None:
            self.Marking_Structure = []
        else:
            self.Marking_Structure = Marking_Structure
        self.Information_Source = Information_Source
    def factory(*args_, **kwargs_):
        if MarkingSpecificationType.subclass:
            return MarkingSpecificationType.subclass(*args_, **kwargs_)
        else:
            return MarkingSpecificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Controlled_Structure(self): return self.Controlled_Structure
    def set_Controlled_Structure(self, Controlled_Structure): self.Controlled_Structure = Controlled_Structure
    def get_Marking_Structure(self): return self.Marking_Structure
    def set_Marking_Structure(self, Marking_Structure): self.Marking_Structure = Marking_Structure
    def add_Marking_Structure(self, value): self.Marking_Structure.append(value)
    def insert_Marking_Structure(self, index, value): self.Marking_Structure[index] = value
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.Controlled_Structure is not None or
            self.Marking_Structure or
            self.Information_Source is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='MarkingSpecificationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MarkingSpecificationType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='marking:', name_='MarkingSpecificationType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            outfile.write(' version=%s' % (self.gds_format_string(quote_attrib(self.version).encode(ExternalEncoding), input_name='version'), ))
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='MarkingSpecificationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Controlled_Structure is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%s:Controlled_Structure>%s</%s:Controlled_Structure>%s' % (nsmap[namespace_], self.gds_format_string(quote_xml(self.Controlled_Structure).encode(ExternalEncoding), input_name='Controlled_Structure'), nsmap[namespace_], eol_))
        for Marking_Structure_ in self.get_Marking_Structure():
            Marking_Structure_.export(outfile, level, nsmap, namespace_, name_='Marking_Structure', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(outfile, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Controlled_Structure':
            Controlled_Structure_ = child_.text
            Controlled_Structure_ = self.gds_validate_string(Controlled_Structure_, node, 'Controlled_Structure')
            self.Controlled_Structure = Controlled_Structure_
        elif nodeName_ == 'Marking_Structure':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "SimpleMarkingStructureType":
                    import stix.bindings.extensions.marking.simple_marking as simple_marking_binding
                    obj_ = simple_marking_binding.SimpleMarkingStructureType.factory()
                elif type_name_ == "TLPMarkingStructureType":
                    import stix.bindings.extensions.marking.tlp as tlp_marking_binding
                    obj_ = tlp_marking_binding.TLPMarkingStructureType.factory()
                elif type_name_ == "TermsOfUseMarkingStructureType":
                    import stix.bindings.extensions.marking.terms_of_use_marking as tou_marking_binding
                    obj_ = tou_marking_binding.TermsOfUseMarkingStructureType.factory()
                else:
                    raise NotImplementedError('Marking structure type not implemented ' + type_name_)
            else:
                raise NotImplementedError('Marking structure type not declared: no xsi_type found')

            obj_.build(child_)
            self.Marking_Structure.append(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
# end class MarkingSpecificationType

GDSClassesMapping = {}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MarkingType'
        rootClass = MarkingType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_=rootTag,
    #     namespacedef_='',
    #     pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MarkingType'
        rootClass = MarkingType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MarkingType'
        rootClass = MarkingType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="MarkingType",
    #     namespacedef_='')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "MarkingType",
    "MarkingStructureType",
    "MarkingSpecificationType"
    ]
