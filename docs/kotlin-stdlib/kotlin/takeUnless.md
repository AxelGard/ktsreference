

# takeUnless

Returns this value if it does not satisfy the given predicate or null, if it does.

```kotlin
inline fun <T> T.takeUnless(predicate: (T) -> Boolean): T?(source)
```

```kotlin
val age = 17
val adult = age.takeUnless { it < 18 }
println(adult) // Prints: null
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/take-unless.html)

    