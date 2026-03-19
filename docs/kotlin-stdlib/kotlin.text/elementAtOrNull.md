

# elementAtOrNull

Returns a character at the given index or null if the index is out of bounds of this char sequence.

```kotlin
inline fun CharSequence.elementAtOrNull(index: Int): Char?(source)
```

```kotlin
fun main() {
    val text = "Hello"

    val charAt1 = text.elementAtOrNull(1)   // 'e'
    val charAt5 = text.elementAtOrNull(10) // null

    println("Character at index 1: $charAt1")   // prints: e
    println("Character at index 10: $charAt5")  // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/element-at-or-null.html)

    