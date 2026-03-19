

# elementAtOrElse

Returns a character at the given index or the result of calling the defaultValue function if the index is out of bounds of this char sequence.

```kotlin
inline fun CharSequence.elementAtOrElse(index: Int, defaultValue: (Int) -> Char): Char(source)
```

```kotlin
fun main() {
    val text = "Hello"
    val index = 10
    val ch = text.elementAtOrElse(index) { '?' }
    println("Character at index $index: $ch") // prints '?'
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/element-at-or-else.html)

    