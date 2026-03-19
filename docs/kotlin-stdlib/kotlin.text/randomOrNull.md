

# randomOrNull

Returns a random character from this char sequence, or null if this char sequence is empty.

```kotlin
inline fun CharSequence.randomOrNull(): Char?(source)
```

```kotlin
fun main() {
    val text = "Kotlin"
    val randomChar = text.randomOrNull()
    println("Random character from \"$text\": $randomChar")

    val emptyText = ""
    val emptyRandom = emptyText.randomOrNull()
    println("Random character from empty string: $emptyRandom")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/random-or-null.html)

    