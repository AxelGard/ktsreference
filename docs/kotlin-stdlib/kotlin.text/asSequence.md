

# asSequence

Creates a Sequence instance that wraps the original char sequence returning its characters when being iterated.

```kotlin
fun CharSequence.asSequence(): Sequence<Char>(source)
```

```kotlin
val text = "Hello, Kotlin!"
text.asSequence()
    .filter { it.isUpperCase() }
    .forEach { println(it) }   // Prints: H, K
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/as-sequence.html)

    