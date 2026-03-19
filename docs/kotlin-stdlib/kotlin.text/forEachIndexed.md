

# forEachIndexed

Performs the given action on each character, providing sequential index with the character.

```kotlin
inline fun CharSequence.forEachIndexed(action: (index: Int, Char) -> Unit)(source)
```

```kotlin
val greeting = "Hello, Kotlin!"

greeting.forEachIndexed { index, char ->
    println("Character at index $index is '$char'")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/for-each-indexed.html)

    