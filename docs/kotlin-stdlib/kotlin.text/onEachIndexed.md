

# onEachIndexed

Performs the given action on each character, providing sequential index with the character, and returns the char sequence itself afterwards.

```kotlin
inline fun <S : CharSequence> S.onEachIndexed(action: (index: Int, Char) -> Unit): S(source)
```

```kotlin
val text = "Kotlin"

text.onEachIndexed { index, char ->
    println("Index $index: $char")
}

println("Original text: $text")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/on-each-indexed.html)

    