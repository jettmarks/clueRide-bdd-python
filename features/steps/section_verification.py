from behave import *

from features.steps.buttons import elements_child_contains_matching_text

use_step_matcher("parse")


@step('I see a "{section_heading_text}" section heading')
def step_impl(context, section_heading_text):
    """
    :param section_heading_text: What the user sees as the Section Heading
    :type context: behave.runner.Context
    """
    heading_list = context.browser.find_elements_by_class_name("section-heading")
    if len(heading_list) == 0:
        raise Exception("No Section Headings Found")

    match_list = [element for element in heading_list
                  if elements_child_contains_matching_text(element, section_heading_text)]
    if len(match_list) == 0:
        raise Exception("No matching Section Heading Found (" + section_heading_text + ")")

    return match_list

