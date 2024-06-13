import pandas as pd
import numpy as np
import streamlit as st
import os
from compare import write_csv_data

st.set_page_config(page_title="Search Comparison", layout="wide")
st.title("Search Comparison")
st.subheader("Plotting search time comparison")


def configure_sidebar():
    with st.sidebar:
        with st.form("my_form"):
            left_border = st.number_input(
                label="Left Border",
                min_value=0,
                max_value=10000,
                value=200,
                step=200,
            )

            right_border = st.number_input(
                label="Right Border",
                min_value=0,
                max_value=50000,
                value=3000,
                step=200,
            )

            step = st.number_input(
                label="Step",
                min_value=0,
                max_value=10000,
                value=100,
                step=200,
            )

            if left_border > left_border or left_border + step > right_border:
                st.error("Right border must be greater than left border")

            submitted = st.form_submit_button(label="Submit", type="primary")

        show_graphics = st.button(label="Show graphics")
        show_data = st.button(label="Show data")

        return {
            "left_border": left_border,
            "right_border": right_border,
            "step": step,
            "submitted": submitted,
            "show_graphics": show_graphics,
            "show_data": show_data,
        }


def get_csv_data(
    left_border, right_border, step, is_full_data=False, with_refreshing=False
):
    if with_refreshing:
        write_csv_data(left_border, right_border, step)

    data = pd.read_csv("search_comparison.csv")
    if is_full_data:
        return data

    number_of_elements = data.iloc[:, 0]
    linear_time = data.iloc[:, 1]
    binary_time = data.iloc[:, 2]
    interpolation_time = data.iloc[:, 3]
    tree_linear_time = data.iloc[:, 4]
    tree_binary_time = data.iloc[:, 5]
    tree_interpolation_time = data.iloc[:, 6]

    return (
        number_of_elements,
        linear_time,
        binary_time,
        interpolation_time,
        tree_linear_time,
        tree_binary_time,
        tree_interpolation_time,
    )


def configure_main_page(
    left_border, right_border, step, submitted, show_graphics, show_data
):
    if submitted or show_graphics:
        if submitted:
            (
                number_of_elements,
                linear_time,
                binary_time,
                interpolation_time,
                tree_linear_time,
                tree_binary_time,
                tree_interpolation_time,
            ) = get_csv_data(
                left_border,
                right_border,
                step,
                with_refreshing=True,
            )
        if show_graphics:
            (
                number_of_elements,
                linear_time,
                binary_time,
                interpolation_time,
                tree_linear_time,
                tree_binary_time,
                tree_interpolation_time,
            ) = get_csv_data(
                left_border,
                right_border,
                step,
            )
        col1, col2 = st.columns(2)

        with col1:
            st.header("Array algorithms")
            chart_data_arr = pd.DataFrame(
                {
                    "Number of Elements": number_of_elements,
                    "Linear Search Time": linear_time,
                }
            )
            st.line_chart(
                chart_data_arr,
                x="Number of Elements",
                y="Linear Search Time",
                color=["#00ff00"],
            )

            st.header("Tree algorithms")
            chart_data_tree = pd.DataFrame(
                {
                    "Number of Elements": number_of_elements,
                    "Tree Linear Search Time": tree_linear_time,
                }
            )
            st.line_chart(
                chart_data_tree,
                x="Number of Elements",
                y="Tree Linear Search Time",
                color=["#00ff00"],
            )

        with col2:
            st.header("")
            chart_data_arr = pd.DataFrame(
                {
                    "Number of Elements": number_of_elements,
                    "Binary Search Time": binary_time,
                    "Interpolation Search Time": interpolation_time,
                }
            )
            st.line_chart(
                chart_data_arr,
                x="Number of Elements",
                color=["#2F3E83", "#E74C3C"],
            )

            st.header("")
            chart_data_tree = pd.DataFrame(
                {
                    "Number of Elements": number_of_elements,
                    "Tree Binary Search Time": tree_binary_time,
                    "Tree Interpolation Search Time": tree_interpolation_time,
                }
            )
            st.line_chart(
                chart_data_tree,
                x="Number of Elements",
                color=["#2F3E83", "#E74C3C"],
            )

    if show_data:
        csv_data = get_csv_data(left_border, right_border, step, is_full_data=True)
        formatted_data = csv_data.map(lambda value: "{:.9f}".format(value))
        st.table(formatted_data)


def main():
    data = configure_sidebar()
    configure_main_page(**data)


if __name__ == "__main__":
    main()
