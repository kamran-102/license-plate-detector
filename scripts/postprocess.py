def english_to_arabic_mapping(input_string):
  eastern_to_western_numerals = {
      '٠': '0',
      '١': '1',
      '٢': '2',
      '٣': '3',
      '٤': '4',
      '٥': '5',
      '٦': '6',
      '٧': '7',
      '٨': '8',
      '٩': '9'
  }

  arabic_to_latin_letters_capital = {
      'ا': 'A',
      'ب': 'B',
      'ح': 'J',
      'د': 'D',
      'ر': 'R',
      'س': 'S',
      'ص': 'X',
      'ط': 'T',
      'ع': 'E',
      'ق': 'G',
      'ك': 'K',
      'ل': 'L',
      'م': 'Z',
      'ن': 'N',
      'هـ': 'H',
      'و': 'U',
      'ى': 'V'
  }
  def map_characters(input_string, western_to_eastern, latin_to_arabic):
      mapped_string = []
      for char in input_string:
          if char.isdigit():
              mapped_string.append(western_to_eastern.get(char, char))
          elif char.isalpha():
              mapped_string.append(latin_to_arabic.get(char, char))
          else:
              mapped_string.append(char)
      return ' '.join(mapped_string)

  # Inverse dictionaries
  western_to_eastern_numerals = {v: k for k, v in eastern_to_western_numerals.items()}
  latin_to_arabic_letters_capital = {v: k for k, v in arabic_to_latin_letters_capital.items()}

  # Mapping the characters
  mapped_string = map_characters(input_string, western_to_eastern_numerals, latin_to_arabic_letters_capital)
  return mapped_string