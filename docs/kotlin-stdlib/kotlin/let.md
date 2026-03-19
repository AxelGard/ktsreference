

# let

Calls the specified function block with this value as its argument and returns its result.

```kotlin
@IgnorableReturnValueinline fun <T, R> T.let(block: (T) -> R): R(source)
```

```kotlin
val email: String? = "user@example.com"

email?.let { 
    val localPart = it.substringBefore("@")
    println("Local part: $localPart")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/let.html)

    