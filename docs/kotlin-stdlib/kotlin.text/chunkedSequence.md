

# chunkedSequence

Splits this char sequence into a sequence of strings each not exceeding the given size.

```kotlin
fun CharSequence.chunkedSequence(size: Int): Sequence<String>(source)
```

```kotlin
fun main() {
    val text = "Hello, world! This is a test."
    for (chunk in text.chunkedSequence(5)) {
        println(chunk)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/chunked-sequence.html)

    