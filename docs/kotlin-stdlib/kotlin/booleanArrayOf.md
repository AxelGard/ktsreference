

# booleanArrayOf

Returns an array containing the specified boolean values.

```kotlin
expect fun booleanArrayOf(vararg elements: Boolean): BooleanArray(source)
```

```kotlin
val flags = booleanArrayOf(true, false, true)

println(flags.size)   // prints 3
println(flags[0])     // prints true
println(flags[1])     // prints false
println(flags[2])     // prints true
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/boolean-array-of.html)

    