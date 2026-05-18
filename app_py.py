{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP9Ndgygt+bxQ3Lk3EYP9FM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/martinezdiemar-afk/proyecto-ia/blob/main/app_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 400
        },
        "id": "5qKR-DOQDl9z",
        "outputId": "bd4122a7-65a2-4a1b-f728-13e526dbb9d7"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'streamlit'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_5882/2150243736.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# Cargar modelo\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import joblib\n",
        "import numpy as np\n",
        "\n",
        "# Cargar modelo\n",
        "model = joblib.load(\"modelo.pkl\")\n",
        "\n",
        "st.title(\"🎓 Predicción de Nota Final (G3)\")\n",
        "\n",
        "st.write(\"Introduce los datos del estudiante:\")\n",
        "\n",
        "# --- Inputs básicos (puedes ampliar luego) ---\n",
        "studytime = st.number_input(\"Tiempo de estudio (1-4)\", min_value=1, max_value=4)\n",
        "failures = st.number_input(\"Número de suspensos anteriores\", min_value=0, max_value=10)\n",
        "absences = st.number_input(\"Faltas de asistencia\", min_value=0, max_value=100)\n",
        "\n",
        "G1 = st.number_input(\"Nota G1\", min_value=0, max_value=20)\n",
        "G2 = st.number_input(\"Nota G2\", min_value=0, max_value=20)\n",
        "\n",
        "# Botón\n",
        "if st.button(\"Predecir G3\"):\n",
        "\n",
        "    # IMPORTANTE: el orden debe ser el mismo que usaste al entrenar el modelo\n",
        "    features = np.array([[studytime, failures, absences, G1, G2]])\n",
        "\n",
        "    pred = model.predict(features)\n",
        "\n",
        "    st.success(f\"🎯 Nota final estimada (G3): {pred[0]:.2f}\")"
      ]
    }
  ]
}