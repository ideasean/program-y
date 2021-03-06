import unittest
import xml.etree.ElementTree as ET

from programy.parser.template.nodes.base import TemplateNode
from programy.parser.template.nodes.map import TemplateMapNode

from test.parser.template.graph.test_graph_client import TemplateGraphTestClient


class TemplateGraphMapTests(TemplateGraphTestClient):

    def test_map_name_as_attrib(self):
        template = ET.fromstring("""
			<template>
				<map name="somemap">sometext</map>
			</template>
			""")
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertEqual(len(ast.children), 1)

        set_node = ast.children[0]
        self.assertIsNotNone(set_node)
        self.assertIsInstance(set_node, TemplateMapNode)
        self.assertIsNotNone(set_node.name)
        self.assertIsInstance(set_node.name, TemplateNode)
        self.assertEqual(set_node.name.resolve(None, None), "somemap")

        self.assertEqual(len(set_node.children), 1)
        self.assertEqual(set_node.children[0].resolve(None, None), "sometext")

    def test_map_name_as_child(self):
        template = ET.fromstring("""
			<template>
				<map><name>somemap</name>sometext</map>
			</template>
			""")
        ast = self.parser.parse_template_expression(template)
        self.assertIsNotNone(ast)
        self.assertIsInstance(ast, TemplateNode)
        self.assertIsNotNone(ast.children)
        self.assertEqual(len(ast.children), 1)

        set_node = ast.children[0]
        self.assertIsNotNone(set_node)
        self.assertIsInstance(set_node, TemplateMapNode)
        self.assertIsNotNone(set_node.name)
        self.assertIsInstance(set_node.name, TemplateNode)
        self.assertEqual(set_node.name.resolve(None, None), "somemap")

        self.assertEqual(len(set_node.children), 1)
        self.assertEqual(set_node.children[0].resolve(None, None), "sometext")


if __name__ == '__main__':
    unittest.main()
