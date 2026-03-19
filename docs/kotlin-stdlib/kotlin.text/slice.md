

# slice

Returns a char sequence containing characters of the original char sequence at the specified range of indices.

```kotlin
fun CharSequence.slice(indices: IntRange): CharSequence(source)
```

```kotlin
val text = "Hello, world!"
val part = text.slice(7..11)   // "world"
println(part)                  // prints: world
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/slice.html)

    