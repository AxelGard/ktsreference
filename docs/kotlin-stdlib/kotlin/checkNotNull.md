

# checkNotNull

Throws an IllegalStateException if the value is null. Otherwise returns the not null value.

```kotlin
@IgnorableReturnValueinline fun <T : Any> checkNotNull(value: T?): T(source)
```

```kotlin
fun main() {
    val nullableName: String? = "Kotlin"
    val name: String = checkNotNull(nullableName)  // throws IllegalStateException if null
    println("Name length: ${name.length}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/check-not-null.html)

    