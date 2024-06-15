import streamlit 
import pandas as pd
import numpy as np


# Criação de dados aleatórios
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

# Exibe os gráficos de linhas
streamlit.line_chart(chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"])
