class SelectorHelper:

    @staticmethod
    def get_parent_of_element(child_element):
        parent_element = child_element.find_element_by_xpath("..")
        return parent_element
