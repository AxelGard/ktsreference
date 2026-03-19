

# setOwner

Sets the file owner to the specified value.

```kotlin
@IgnorableReturnValueinline fun Path.setOwner(value: UserPrincipal): Path(source)
```

```kotlin
import java.nio.file.Paths
import java.nio.file.attribute.UserPrincipal
import kotlin.io.path.setOwner

fun main() {
    val path = Paths.get("/tmp/example.txt")
    val user: UserPrincipal =
        path.fileSystem.userPrincipalLookupService().lookupPrincipalByName("bob")
    path.setOwner(user)   // the returned Path is ignored
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/set-owner.html)

    