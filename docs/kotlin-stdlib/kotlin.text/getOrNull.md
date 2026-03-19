

# getOrNull

Returns a character at the given index or null if the index is out of bounds of this char sequence.

```kotlin
fun CharSequence.getOrNull(index: Int): Char?(source)
```

```kotlin
fun main() {
    val text = "Kotlin"

    // Get the character at index 2 (the third character)
    val charAt2 = text.getOrNull(2)   // 't'
    println("Character at index 2: $charAt2")

    // Try to get a character at an out‑of‑bounds index
    val charAt10 = text.getOrNull(10) // null
    println("Character at index 10: ${charAt10 ?: "Index out of bounds"}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/get-or-null.html)

    