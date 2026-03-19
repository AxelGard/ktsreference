

# plus

Concatenates this Char and a String.

```kotlin
inline operator fun Char.plus(other: String): String(source)
```

```kotlin
fun main() {
    val char: Char = 'H'
    val text: String = "ello"
    val greeting = char + text   // 'H' + "ello" -> "Hello"
    println(greeting)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/plus.html)

    