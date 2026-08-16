{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMtaWQalitBC23+yk4kF63e",
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
        "<a href=\"https://colab.research.google.com/github/qaiserbangash54-dotcom/data-engineering-journey/blob/main/password_generator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rSpd0SEgA1p5",
        "outputId": "5e7d129d-4c35-4c3e-f697-727fe4c1ca0b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Aapka strong password hai: \\87q`0&Z<Vz]\n"
          ]
        }
      ],
      "source": [
        "#Hi let's start with the project of password Generator\n",
        "#So first of all we will import random for chossing any\n",
        "#characters from the characters given by the string function\n",
        "#and for the charcter we shall go for string import\n",
        "\n",
        "import random\n",
        "import string\n",
        "\n",
        "def generate_password(length=12):\n",
        "    letters = string.ascii_letters\n",
        "    digits = string.digits\n",
        "    symbols = string.punctuation\n",
        "\n",
        "    # first of all we shall gaurentee that each type will have 1 letter\n",
        "    password = [\n",
        "        random.choice(string.ascii_lowercase),  # 1 small letter\n",
        "        random.choice(string.ascii_uppercase),  # 1 capital letter\n",
        "        random.choice(digits),                  # 1 number\n",
        "        random.choice(symbols)                  # 1 symbol\n",
        "    ]\n",
        "\n",
        "    # Fill the remaining length with random characters.\n",
        "    all_characters = letters + digits + symbols\n",
        "    for i in range(length - 4):\n",
        "        password.append(random.choice(all_characters))\n",
        "\n",
        "    # Shuffle the order to prevent a predictable pattern.\n",
        "    random.shuffle(password)\n",
        "\n",
        "    # Join the list back into a string\n",
        "    return ''.join(password)\n",
        "\n",
        "new_password = generate_password(12)\n",
        "print(\"Aapka strong password hai:\", new_password)\n"
      ]
    }
  ]
}