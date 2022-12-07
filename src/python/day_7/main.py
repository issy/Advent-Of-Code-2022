from __future__ import annotations

import os
import re
from typing import Optional


class Node:
    name: str
    parent: Optional[Node]
    children: list[Node]
    files: list[tuple[int, str]]

    def __init__(self, name: str, parent: Optional[Node] = None):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def add_file(self, file_size: int, file_name: str):
        self.files.append((file_size, file_name))

    def add_child(self, name: str):
        self.children.append(Node(name, self))

    def get_child(self, name: str) -> Optional[Node]:
        for child in self.children:
            if child.name == name:
                return child

    def get_qualified_path(self) -> str:
        path = self.name
        parent = self.parent
        while parent is not None:
            path = f"{parent.name}/{path}"
            parent = parent.parent

        return path

    def get_immediate_directory_size(self) -> int:
        return sum(map(lambda f: f[0], self.files))

    def get_total_directory_size(self) -> int:
        total = self.get_immediate_directory_size()
        for child in self.children:
            total += child.get_total_directory_size()

        return total


def create_nodes(lines: list[str]) -> Node:
    root_node = Node("/")
    current_node = root_node
    for line in lines:
        if line.startswith("$ cd "):
            (name,) = re.match("^\$ cd (.+)$", line).groups()
            if name == "..":
                current_node = current_node.parent
            else:
                current_node = current_node.get_child(name)
        elif line == "$ ls":
            continue
        elif line.startswith("dir"):
            (name,) = re.match("^dir (.+)$", line).groups()
            current_node.add_child(name)
        else:
            (file_size, file_name) = re.match("^(\d+) (.+)$", line).groups()
            current_node.add_file(int(file_size), file_name)

    return root_node


def enumerate_nodes(node: Node) -> list[Node]:
    nodes = []
    for child in node.children:
        nodes.append(child)
        nodes.extend(enumerate_nodes(child))

    return nodes


def part_1(inp: str) -> int:
    lines = inp.splitlines()[1:]
    root_node = create_nodes(lines)
    all_nodes = enumerate_nodes(root_node)
    return sum(filter(lambda s: s <= 100000, map(Node.get_total_directory_size, all_nodes)))


def part_2(inp: str) -> int:
    lines = inp.splitlines()[1:]
    capacity = 70000000
    required_space = 30000000

    root_node = create_nodes(lines)
    used_space = root_node.get_total_directory_size()
    required_minimum_size = used_space - (capacity - required_space)

    all_nodes = enumerate_nodes(root_node)
    return sorted(filter(lambda s: s >= required_minimum_size, map(Node.get_total_directory_size, all_nodes)))[0]


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    with open(f"../../../common/{os.path.split(os.getcwd())[-1]}/input.txt", "r") as fp:
        inp = fp.read()

    part_1_result = part_1(inp)
    print("part 1 result:", part_1_result)

    part_2_result = part_2(inp)
    print("part 2 result:", part_2_result)
