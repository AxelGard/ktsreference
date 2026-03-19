

# endsWith

Returns true if this char sequence ends with the specified character.

```kotlin
fun CharSequence.endsWith(char: Char, ignoreCase: Boolean = false): Boolean(source)
```

```kotlin
fun main() {
    val word = "Kotlin"

    println(word.endsWith('n'))               // true
    println(word.endsWith('N'))               // false
    println(word.endsWith('N', ignoreCase = true)) // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/ends-with.html)

    