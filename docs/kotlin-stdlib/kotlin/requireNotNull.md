

# requireNotNull

Throws an IllegalArgumentException if the value is null. Otherwise returns the not null value.

```kotlin
@IgnorableReturnValueinline fun <T : Any> requireNotNull(value: T?): T(source)
```

fun greet(name: String?) {
    val actualName = requireNotNull(name) { "Name must not be null" }
    println("Hello, $actualName!")
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/require-not-null.html)

    