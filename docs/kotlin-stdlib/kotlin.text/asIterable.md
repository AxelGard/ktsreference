

# asIterable

Creates an Iterable instance that wraps the original char sequence returning its characters when being iterated.

```kotlin
fun CharSequence.asIterable(): Iterable<Char>(source)
```

```kotlin
fun main() {
    val text = "Kotlin"
    for (c in text.asIterable()) {
        println(c)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/as-iterable.html)

    