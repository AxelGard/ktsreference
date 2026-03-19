

# takeIf

Returns this value if it satisfies the given predicate or null, if it doesn't.

```kotlin
inline fun <T> T.takeIf(predicate: (T) -> Boolean): T?(source)
```

```kotlin
val number = 10

val evenNumber = number.takeIf { it % 2 == 0 }   // returns 10
val oddNumber  = number.takeIf { it % 2 != 0 }   // returns null

println("evenNumber = $evenNumber")  // evenNumber = 10
println("oddNumber  = $oddNumber")   // oddNumber  = null
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/take-if.html)

    