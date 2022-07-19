# -*- coding: utf-8 -*-
'''
Documentation: - Delete when complete
* Talk to 'Future You' readint the methods and classes 6/8 months from now.
* Future you has spent those months on 5/6 other projects and cant
remember any of this.
* Future you doesn't have time to spend a full day trying to 'get
into' the code in order to fix a bug / adapt a method.
* Be Generous to future you, that will be you some day.

DESCRIPTION:

Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

:Author: Tom
:Created: 17/07/2022
:Copyright: Tom Welsh - twelsh37@gmail.com
'''
import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_authenticator as stauth


# Our Main function
def main():

    # Column setup
    col1, col2 = st.columns(2)

    with col1:
        df2 = pd.read_csv('africanparks.csv')
        st.title("A Selection of African Game Parks")
        fig = px.scatter_mapbox(df2,
                                lat='latitude',
                                lon='longitude',
                                color=df2['name'],
                                size_max=20,
                                width=800,
                                height=800,
                                custom_data=[df2['name']]
                                )
        # Set the center point of the map and the starting zoom
        fig.update_mapboxes(center=dict(lat=5, lon=24),
                            zoom=2
                            )
        fig.update_layout(showlegend=False)
        fig.update_traces(
            # This removed the colorbar
            marker_coloraxis=None,
            hovertemplate='<B>Name: </B>'
        )
        # Plot!
        st.plotly_chart(fig, use_container_width=True, width=800, height=600)
    with col2:
        st.title("Mapping Information")
        st.write(df2.head(10))

    # show streamlit sidebar
    st.sidebar.success("Select a demo above.")


if __name__ == '__main__':
    main()
