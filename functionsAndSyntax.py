# A barra invertida (\) tem um significado quando usada dentro de strings – isso é chamado de caractere de escape
print("A aranha pequenininha\nsubiu a tromba d'água.")

print()

# A barra invertida é apenas um tipo de anúncio de que o próximo caractere após a barra invertida também tem um significado diferente
# A letra "n" colocada após a barra invertida vem da palavra newline (nova linha)
print("abaixo veio a chuva\ne lavou a aranha.")

# Colocar apenas uma barra invertida dentro de uma string gera erro
print("\")
      
# Devido a sua natureza de escape - é necessário dobrá-lo
print("\\")

# Nem todo caractere após a barra invertida significa algo
print("A aranha p\equenininha\nsubiu a tromba d'água.")

# Argumentos de palavra-chave alteram o comportemento de uma função print()
print("Meu", "nome", "é", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Programação","Essenciais","em", sep="***", end="...")
print("Python", end=" ")

# Solução de amostra (Formatação de saída)

###################
print("versão original:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("com menos 'print()' invocações:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("mais alto:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("dobrou:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)
