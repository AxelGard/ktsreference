

# isBlank

Returns true if this char sequence is empty or consists solely of whitespace characters according to Char.isWhitespace.

```kotlin
fun CharSequence.isBlank(): Boolean(source)
```

```kotlin
fun main() {
    val strings = listOf("   ", "\t\n", "", "Kotlin", "  Kotlin  ")

    strings.forEach { s ->
        println("\"$s\" is blank: ${s.isBlank()}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-blank.html)

    