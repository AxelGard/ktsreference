

# assert

Throws an AssertionError if the value is false and runtime assertions have been enabled on the JVM using the -ea JVM option.

```kotlin
inline fun assert(value: Boolean)(source)
```

```kotlin
fun main() {
    val a = 10
    val b = 5

    // Simple assertion using the inline assert with a lazy message
    assert(a > b) { "Expected a ($a) to be greater than b ($b)" }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/assert.html)

    