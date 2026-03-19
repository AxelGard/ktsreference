

# forEach

Performs the given action on each element.

```kotlin
inline fun <T> Sequence<T>.forEach(action: (T) -> Unit)(source)
```

```kotlin
val words = listOf("apple", "banana", "cherry").asSequence()

words.forEach { word ->
    println(word.uppercase())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/for-each.html)

    