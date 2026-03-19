

# assert

Throws an AssertionError if the value is false and runtime assertions have been enabled on the JVM using the -ea JVM option.

```kotlin
inline fun assert(value: Boolean)(source)
```

fun main() {
    val number = 42
    assert(number > 0)
    println("Number is positive")
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/assert.html)

    